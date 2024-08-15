import logging
import re
import requests
from urllib.parse import urlparse, parse_qs
from flask import make_response

logger = logging.getLogger(__name__)
from superset import app


class IChangAnUtil:
    def __init__(self, url):
        self.url = url
        self.query_parameters = self._parse_url()

    def _parse_url(self):
        return parse_qs(urlparse(self.url).query)

    @property
    def get_dashboard_id(self):
        rq_path = urlparse(self.url).path
        dashboard_pattern = re.compile(r'/dashboard/(\d+)/')
        if result := dashboard_pattern.search(rq_path):
            return result.group(1)

    @property
    def get_token(self):
        token = self.query_parameters.get('token', [None])[0]
        if token is None:
            token = self.query_parameters.get('IdentityToken', [None])[0]
        return token

    @property
    def get_employee_number(self):
        return self.query_parameters.get('employeenumber', [None])[0]

    def get_user_by_token(self) -> str:
        if check_url := app.config.get('USER_BY_TOKEN_URL'):
            try:
                response = requests.get(
                    check_url,
                    params={'identityToken': self.get_token}
                )
                return self._get_login_id(response)
            except Exception as e:
                logger.error(e)

    def get_cmp_user_by_token(self) -> str:
        if check_url := app.config.get('CMP_GET_USER_BY_TOKEN'):
            try:
                response = requests.get(
                    url=check_url,
                    params={'identityToken': self.get_token},
                    timeout=20
                )
                return self._get_login_id(response)
            except Exception as e:
                logger.error(e)

    @staticmethod
    def _get_login_id(response):
        if response.status_code == 200:
            json_data = response.json() or {}
            res_code = json_data.get('result')
            if res_code == '200':
                data = json_data.get("data", {})
                user_enabled = data.get("enabled", False)
                if user_enabled:
                    return data.get('loginID')
                else:
                    logger.warning(f"Current User Disabled!")
                    return make_response("User Disabled!", 401)
            else:
                logger.error(
                    f'Authentication error {res_code}: {json_data.get("errorMsg")}')
        else:
            logger.error('Authentication server connection error')

    def check_user_by_login_id(self) -> bool:
        return self.get_user_by_token() == self.get_employee_number is not None

