#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import logging
from logging import handlers
from common.config_utils import config

log_path = os.path.join(os.path.dirname(__file__),'..',config.LOG_PATH)

class LogUtils:
    def __init__(self,log_path=log_path):
        self.log_file_name = 'API_TEST_LOG.log'
        self.logger = logging.getLogger('lcf')
        self.logger.setLevel(config.LOG_LEVEL)
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        console_hanlder = logging.StreamHandler()
        console_hanlder.setFormatter(formatter)
        console_hanlder.setLevel(config.LOG_LEVEL)

        file_hanlder = handlers.TimedRotatingFileHandler(os.path.join(log_path,self.log_file_name),when='D',interval=1,backupCount=7)
        file_hanlder.setLevel(config.LOG_LEVEL)
        file_hanlder.setFormatter(formatter)

        self.logger.addHandler(console_hanlder)
        self.logger.addHandler(file_hanlder)

        console_hanlder.close() # 防止打印日志重复
        file_hanlder.close()

    def get_logger(self):
        return self.logger  # 自己返回自己

logger = LogUtils().get_logger()

if __name__=='__main__':
    logger.warning('警告')