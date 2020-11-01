#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename='test.log')
logging.debug('-----调试信息[debug]-----')
logging.info('-----有用的信息[info]-----')
logging.warning('-----警告信息[warning]-----')
logging.error('-----错误信息[error]-----')
logging.critical('-----严重错误信息[critical]-----')