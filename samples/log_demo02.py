#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging

# 过程：设置日志格式，等级--> 设置handler对象 --> 加载到logger对象

logger = logging.getLogger('test_lcf')
logger.setLevel(logging.DEBUG)    #设置默认的日志级别
#创建日志格式对象
con_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(message)s')

sh = logging.StreamHandler() #创建StreamHandler控制台输出对象
sh.setFormatter(con_formatter) #StreamHandler对象自定义日志格式
sh.setLevel(logging.DEBUG) #StreamHandler对象自定义日志级别

fh = logging.FileHandler('test.log','a',encoding='utf-8')
fh.setFormatter( file_formatter )
fh.setLevel( logging.DEBUG )

logger.addHandler(sh)
logger.addHandler(fh) #logger日志对象加载StreamHandler对象
logger.info('李传风')   #日志输出

# 设置日志格式、等级 == setFormatter setLevel 》 设置Handler对象  == addHandler 》加载到logger对象


