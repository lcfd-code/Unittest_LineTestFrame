#!/usr/bin/python
# -*- coding:utf-8 -*-

from nb_log import LogManager

logger = LogManager('lcf').get_logger_and_add_handlers()

logger.debug('p1')
logger.info('p2')
logger.warning('p3')
logger.error('p4')
logger.critical('p5')
# print('hello')