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

import logging
import os
import time
from logging import handlers
from pathlib import Path


class SafeTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))

        # 存在删除逻辑去掉
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt

    def rotate(self, source, dest):
        if not callable(self.rotator):
            # 增加os.path.exists(dest)，如果目标存在，不再rename
            if os.path.exists(source):
                if not os.path.exists(dest):
                    os.rename(source, dest)
        else:
            self.rotator(source, dest)


def setup_log(name=None):
    log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(filename)s[%(lineno)s] -%(funcName)s\n%(message)s')

    # file handler
    # file_name = os.path.join('log_{}.log'.format(name))
    # file_handler = logging.handlers.RotatingFileHandler(
    #     './monitorlog/' + file_name, mode='a', maxBytes=20 * 1024 * 1024,
    #     encoding='utf8', delay=0)
    # file_handler.setFormatter(log_formatter)

    # time file handler; 保存7天的数据

    daily_file_name = str(Path(__file__).parent.parent.joinpath('monitorlog').joinpath('daily_log_{}.log'.format(name)))
    # 每日23:59切换文件，避免与0点的任务冲突
    daily_file_handler = SafeTimedRotatingFileHandler(
        daily_file_name, when='MIDNIGHT', backupCount=0,
        encoding='utf8')
    daily_file_handler.setFormatter(log_formatter)

    # stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)

    # root log
    g_logger = logging.getLogger()
    g_logger.setLevel(logging.DEBUG)
    if not g_logger.handlers:
        # g_logger.addHandler(file_handler)
        g_logger.addHandler(stream_handler)
        g_logger.addHandler(daily_file_handler)
    return g_logger


log = setup_log("monitor")
