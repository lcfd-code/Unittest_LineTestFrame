#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import time
from logging import handlers

logger = logging.getLogger('test_lcf')
logger.setLevel(logging.DEBUG)    #设置默认的日志级别

# 日志切割，设置每天生成一个日志文件
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
th = handlers.TimedRotatingFileHandler('test',when='S',interval=3,backupCount=5)
th.setFormatter(formatter)
th.setLevel( logging.DEBUG )
th.suffix = "%Y%m%d.log" # 日志名格式

logger.addHandler(th)
time.sleep(4)
logger.warning('lcf01')
time.sleep(4)
logger.error('lcf02')