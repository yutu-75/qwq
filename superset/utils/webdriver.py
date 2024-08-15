# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# ------------------------------------------------------------------
# File Name:        webdriver.py
# Author:           王邦权
# Version:          webdriver-001
# Created:          2023/6/14
# Rows:             163
# Description:      重写 selenium屏幕截图函数 get_screenshot
#                   保留原有 get_screenshot 重命名为 get_screenshot_old
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# File Name:        webdriver.py
# Author:           王邦权
# Version:          webdriver-002
# Created:          2023/6/14
# Rows:             233
# Description:      添加 selenium+pdfkit 生成pdf函数 get_pdf
# ------------------------------------------------------------------

from __future__ import annotations

import logging
from enum import Enum
from time import sleep
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

from flask import current_app
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver import chrome, firefox, FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from superset.extensions import machine_auth_provider_factory
from superset.utils.retries import retry_call
from superset.v2.utils.water_mark_utils import WaterMark
from superset.v2.utils.wkhtmltopdf_utils import wk_to_pdf_binary_by_html

WindowSize = Tuple[int, int]
logger = logging.getLogger(__name__)


if TYPE_CHECKING:
    from flask_appbuilder.security.sqla.models import User


class DashboardStandaloneMode(Enum):
    HIDE_NAV = 1
    HIDE_NAV_AND_TITLE = 2
    REPORT = 3


class ChartStandaloneMode(Enum):
    HIDE_NAV = "true"
    SHOW_NAV = 0


def find_unexpected_errors(driver: WebDriver) -> List[str]:
    error_messages = []

    try:
        alert_divs = driver.find_elements(By.XPATH, "//div[@role = 'alert']")
        logger.debug(
            "%i alert elements have been found in the screenshot", len(alert_divs)
        )

        for alert_div in alert_divs:
            # See More button
            alert_div.find_element(By.XPATH, ".//*[@role = 'button']").click()

            # wait for modal to show up
            modal = WebDriverWait(
                driver, current_app.config["SCREENSHOT_WAIT_FOR_ERROR_MODAL_VISIBLE"]
            ).until(
                EC.visibility_of_any_elements_located(
                    (By.CLASS_NAME, "ant-modal-content")
                )
            )[
                0
            ]

            err_msg_div = modal.find_element(By.CLASS_NAME, "ant-modal-body")

            # collect error message
            error_messages.append(err_msg_div.text)

            # close modal after collecting error messages
            modal.find_element(By.CLASS_NAME, "ant-modal-close").click()

            # wait until the modal becomes invisible
            WebDriverWait(
                driver, current_app.config["SCREENSHOT_WAIT_FOR_ERROR_MODAL_INVISIBLE"]
            ).until(EC.invisibility_of_element(modal))

            # Use HTML so that error messages are shown in the same style (color)
            error_as_html = err_msg_div.get_attribute("innerHTML").replace("'", "\\'")

            try:
                # Even if some errors can't be updated in the screenshot,
                # keep all the errors in the server log and do not fail the loop
                driver.execute_script(
                    f"arguments[0].innerHTML = '{error_as_html}'", alert_div
                )
            except WebDriverException:
                logger.warning(
                    "Failed to update error messages using alert_div", exc_info=True
                )
    except WebDriverException:
        logger.warning("Failed to capture unexpected errors", exc_info=True)

    return error_messages


class WebDriverProxy:
    def __init__(self, driver_type: str, window: Optional[WindowSize] = None):
        self._driver_type = driver_type
        self._window: WindowSize = window or (800, 600)
        self._screenshot_locate_wait = current_app.config["SCREENSHOT_LOCATE_WAIT"]
        self._screenshot_load_wait = current_app.config["SCREENSHOT_LOAD_WAIT"]

    def create(self) -> WebDriver:
        pixel_density = current_app.config["WEBDRIVER_WINDOW"].get("pixel_density", 1)
        if self._driver_type == "firefox":
            driver_class = firefox.webdriver.WebDriver
            options = firefox.options.Options()
            profile = FirefoxProfile()
            profile.set_preference("layout.css.devPixelsPerPx", str(pixel_density))
            kwargs: Dict[Any, Any] = dict(options=options, firefox_profile=profile)
        elif self._driver_type == "chrome":
            driver_class = chrome.webdriver.WebDriver
            options = chrome.options.Options()
            options.add_argument(f"--force-device-scale-factor={pixel_density}")
            options.add_argument(f"--window-size={self._window[0]},{self._window[1]}")
            kwargs = dict(options=options)
        else:
            raise Exception(f"Webdriver name ({self._driver_type}) not supported")
        # Prepare args for the webdriver init

        # Add additional configured options
        for arg in current_app.config["WEBDRIVER_OPTION_ARGS"]:
            options.add_argument(arg)

        kwargs.update(current_app.config["WEBDRIVER_CONFIGURATION"])
        logger.info("Init selenium driver")

        return driver_class(**kwargs)

    def auth(self, user: User) -> WebDriver:
        driver = self.create()
        return machine_auth_provider_factory.instance.authenticate_webdriver(
            driver, user
        )

    @staticmethod
    def destroy(driver: WebDriver, tries: int = 2) -> None:
        """Destroy a driver"""
        # This is some very flaky code in selenium. Hence the retries
        # and catch-all exceptions
        try:
            retry_call(driver.close, max_tries=tries)
        except Exception:  # pylint: disable=broad-except
            pass
        try:
            driver.quit()
        except Exception:  # pylint: disable=broad-except
            pass

    def get_screenshot_old(
            self, url: str, element_name: str, user: User
    ) -> Optional[bytes]:
        driver = self.auth(user)
        driver.set_window_size(*self._window)
        driver.get(url)
        img: Optional[bytes] = None
        selenium_headstart = current_app.config["SCREENSHOT_SELENIUM_HEADSTART"]
        logger.debug("Sleeping for %i seconds.", selenium_headstart)
        sleep(selenium_headstart)

        try:
            logger.debug("Wait for the presence of %s..", element_name)
            element = WebDriverWait(driver, self._screenshot_locate_wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_name))
            )

            logger.debug("Wait for chart containers to draw.")
            WebDriverWait(driver, self._screenshot_locate_wait).until(
                EC.visibility_of_all_elements_located(
                    (By.CLASS_NAME, "slice_container")
                )
            )

            logger.debug("Wait for loading element of charts to be gone.")
            WebDriverWait(driver, self._screenshot_load_wait).until_not(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "loading"))
            )

            selenium_animation_wait = current_app.config[
                "SCREENSHOT_SELENIUM_ANIMATION_WAIT"
            ]
            logger.debug("Wait %i seconds for chart animation.", selenium_animation_wait)
            sleep(selenium_animation_wait)
            logger.info(
                "Taking a PNG screenshot of url %s as user %s.",
                url,
                user.username,
            )

            if current_app.config["SCREENSHOT_REPLACE_UNEXPECTED_ERRORS"]:
                unexpected_errors = find_unexpected_errors(driver)
                if unexpected_errors:
                    logger.warning(
                        "%i errors found in the screenshot. URL: %s. Errors are: %s.",
                        len(unexpected_errors),
                        url,
                        unexpected_errors,
                    )

            img = element.screenshot_as_png

        except TimeoutException:
            logger.warning("Selenium timed out requesting url %s.", url, exc_info=True)
        except StaleElementReferenceException:
            logger.error(
                "Selenium got a stale element while requesting url %s.",
                url,
                exc_info=True,
            )
        except WebDriverException as ex:
            logger.error(ex, exc_info=True)
        finally:
            self.destroy(driver, current_app.config["SCREENSHOT_SELENIUM_RETRIES"])
        return img

    def get_screenshot(
            self, url: str, element_name: str, user: User, creator: User = None
    ) -> Optional[bytes]:
        """
            selenium 截图
        """

        driver = self.create()
        # 登录账号
        driver.get(current_app.config["V2_SELENIUM_LOGIN_URL"])
        sleep(current_app.config["V2_SELENIUM_COMMON_SLEEP_TIME"])
        driver.find_element_by_id('username').send_keys(current_app.config["V2_SELENIUM_ADMIN_USERNAME"])
        driver.find_element_by_id('pwd').send_keys(current_app.config["V2_SELENIUM_ADMIN_PASSWORD"])
        sleep(current_app.config["V2_SELENIUM_COMMON_SLEEP_TIME"])
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/button/span').click()
        sleep(current_app.config["V2_SELENIUM_COMMON_SLEEP_TIME"])

        driver.set_window_size(*self._window)
        driver.get(url)
        img: Optional[bytes] = None
        selenium_headstart = current_app.config["SCREENSHOT_SELENIUM_HEADSTART"]
        logger.debug("Sleeping for %i seconds", selenium_headstart)
        sleep(selenium_headstart)

        try:
            logger.debug("Wait for the presence of %s", element_name)
            element = WebDriverWait(driver, self._screenshot_locate_wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_name))
            )
            logger.debug("Wait for chart containers to draw..")
            WebDriverWait(driver, self._screenshot_locate_wait).until(
                EC.visibility_of_all_elements_located(
                    (By.CLASS_NAME, "slice_container")
                )
            )
            logger.debug("Wait for loading element of charts to be gone..")
            WebDriverWait(driver, self._screenshot_load_wait).until_not(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "loading"))
            )
            selenium_animation_wait = current_app.config[
                "SCREENSHOT_SELENIUM_ANIMATION_WAIT"
            ]
            logger.debug("Wait %i seconds for chart animation..", selenium_animation_wait)
            sleep(selenium_animation_wait)
            logger.info(
                "Taking a PNG screenshot of url %s as user %s..",
                url,
                user.username,
            )
            if current_app.config["SCREENSHOT_REPLACE_UNEXPECTED_ERRORS"]:
                unexpected_errors = find_unexpected_errors(driver)
                if unexpected_errors:
                    logger.warning(
                        "%i errors found in the screenshot. URL: %s. Errors are: %s..",
                        len(unexpected_errors),
                        url,
                        unexpected_errors,
                    )

            # img = element.screenshot_as_png
            img = element.screenshot_as_base64

            # 加水印
            img = WaterMark(creator).add_mark(
                in_type='img_base64', out_type='img_binary', in_data=img)

        except TimeoutException:
            logger.warning("Selenium timed out requesting url %s..", url, exc_info=True)
        except StaleElementReferenceException:
            logger.error(
                "Selenium got a stale element while requesting url %s..",
                url,
                exc_info=True,
            )
        except WebDriverException as ex:
            logger.error(ex, exc_info=True)
        finally:
            # 关闭驱动
            self.destroy(driver, current_app.config["SCREENSHOT_SELENIUM_RETRIES"])
        return img

    def get_pdf(
            self, url: str, element_name: str, user: User
    ) -> Optional[bytes]:
        """
            通过selenium获取pdf截图
        """
        driver = self.create()

        # 登录账号
        driver.get(current_app.config["V2_SELENIUM_LOGIN_URL"])
        sleep(current_app.config["V2_SELENIUM_COMMON_SLEEP_TIME"])
        driver.find_element_by_id('username').send_keys(current_app.config["V2_SELENIUM_ADMIN_USERNAME"])
        driver.find_element_by_id('pwd').send_keys(current_app.config["V2_SELENIUM_ADMIN_PASSWORD"])
        sleep(current_app.config["V2_SELENIUM_COMMON_SLEEP_TIME"])
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[4]/button/span').click()
        sleep(current_app.config["V2_SELENIUM_COMMON_SLEEP_TIME"])

        driver.set_window_size(*self._window)
        driver.get(url)
        pdf: Optional[bytes] = None
        selenium_headstart = current_app.config["SCREENSHOT_SELENIUM_HEADSTART"]
        logger.debug("Sleeping for %i seconds..", selenium_headstart)
        sleep(selenium_headstart)

        try:
            logger.debug("Wait for the presence of %s.", element_name)
            element = WebDriverWait(driver, self._screenshot_locate_wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_name))
            )

            logger.debug("Wait for chart containers to draw")
            WebDriverWait(driver, self._screenshot_locate_wait).until(
                EC.visibility_of_all_elements_located(
                    (By.CLASS_NAME, "slice_container")
                )
            )

            logger.debug("Wait for loading element of charts to be gone")
            WebDriverWait(driver, self._screenshot_load_wait).until_not(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "loading"))
            )

            selenium_animation_wait = current_app.config[
                "SCREENSHOT_SELENIUM_ANIMATION_WAIT"
            ]
            logger.debug("Wait %i seconds for chart animation", selenium_animation_wait)
            sleep(selenium_animation_wait)
            logger.info(
                "Taking a PNG screenshot of url %s as user %s",
                url,
                user.username,
            )

            if current_app.config["SCREENSHOT_REPLACE_UNEXPECTED_ERRORS"]:
                unexpected_errors = find_unexpected_errors(driver)
                if unexpected_errors:
                    logger.warning(
                        "%i errors found in the screenshot. URL: %s. Errors are: %s",
                        len(unexpected_errors),
                        url,
                        unexpected_errors,
                    )

            # pdfkit 生成pdf
            # base64拼装成html
            source_text = f'<img src="data:image/png;base64,{element.screenshot_as_base64}"/>'
            # 通过html生成pdf 二进制流
            pdf = wk_to_pdf_binary_by_html(source_text)

            # 加水印
            pdf = WaterMark().add_mark(in_type='pdf_binary', out_type='pdf_binary', in_data=pdf)

        except TimeoutException:
            logger.warning("Selenium timed out requesting url %s", url, exc_info=True)
        except StaleElementReferenceException:
            logger.error(
                "Selenium got a stale element while requesting url %s",
                url,
                exc_info=True,
            )
        except WebDriverException as ex:
            logger.error(ex, exc_info=True)
        finally:
            # 关闭驱动
            self.destroy(driver, current_app.config["SCREENSHOT_SELENIUM_RETRIES"])
        return pdf
