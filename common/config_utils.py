#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import configparser

# 路径的配置加载一般放在类前面
config_file_path = os.path.join(os.path.dirname(__file__),'..','config','localconfig.ini')

class ConfigUtils:
    def __init__(self,conf_path = config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_file_path)

    @property  # 类中的一个方法加property装饰器，变成属性方法
    def HOSTS(self):
        hosts_value = self.cfg.get('default','HOSTS')
        return hosts_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('default','REPORT_PATH')
        return report_path_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('default','REPORT_PATH')
        return report_path_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('default','LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int(self.cfg.get('default','LOG_LEVEL'))
        return log_level_value

    @property
    def SMTP_SENDER(self):
        smtp_sender_value = self.cfg.get('default','SMTP_SENDER')
        return smtp_sender_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('default','SMTP_RECEIVER')
        return smtp_receiver_value

config = ConfigUtils()
if __name__ == '__main__': # 1调试模块代码，2防止重复调用

    print(config.SMTP_SENDER)