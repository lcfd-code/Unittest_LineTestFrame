#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import unittest
import json
from common.config_utils import config
from common import api_info
from common.log_utils import logger

class TestCreateTagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_create_tag(self):
        self._testMethodName = 'case05'
        self._testMethodDoc = '验证create_tag接口是否正常'
        logger.info('case02 验证test_create_tag接口是否正常 --开始执行--')
        token_id = api_info.get_access_token_value(self.session, self.HOSTS)
        # 创建标签
        post_data = {   "tag" : {     "name" : "圣罗3"} }
        response = api_info.test_create_tag(self.session,self.HOSTS,token_id,post_data)
        actula_result = response.json()['tag']['name']
        logger.info('case02 验证test_create_tag接口是否正常 --执行结束--')
        self.assertEqual(actula_result,'圣罗3','case05 验证create_tag接口是否正常处理')
"""
    def test_create_tag_error(self):
        self._testMethodName = 'case06'
        self._testMethodDoc = '验证create_tag接口标签名非法时是否正常处理'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wxb4f279bf92396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)

        token_id = response.json()['access_token']
        post_data = {   "tag" : {     "name" : "李传风01"} }
        response = self.session.post(url=' https://%s/cgi-bin/tags/create?access_token=%s'%(self.HOSTS,token_id),
                                     json=post_data)
        print(response.json())
        actula_result = response.json()['errcode']

        self.assertEqual(actula_result,45157,'case06 验证create_tag接口标签名非法或重复时是否正常处理')
"""
if __name__ == '__main__':
    unittest.main(verbosity=2)