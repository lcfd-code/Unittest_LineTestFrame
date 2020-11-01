#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import unittest
from common.config_utils import config

class TestDelectTagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_delect_tag(self):
        self._testMethodName = 'case07'
        self._testMethodDoc = '验证test_delect_tag接口是否正常'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wxb4f279bf92396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)
        token_id = response.json()['access_token']
        # print(token_id)
        post_data = {   "tag":{        "id" : 134   } }
        response = self.session.post(url='https://%s/cgi-bin/tags/delete?access_token=%s'%(self.HOSTS,token_id),
                                    json=post_data)
        actula_result = response.json()['errmsg']
        print(response.json())
        self.assertEqual(actula_result,"ok", 'case07 验证test_delect_tag接口是否正常')

    def test_delect_tag_error(self):
        self._testMethodName = 'case08'
        self._testMethodDoc = '验证test_delect_tag_error接口是否正常'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wxb4f279bf92396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token' % self.HOSTS,
                                    params=get_param_dict)
        token_id = response.json()['access_token']
        # print(token_id)
        post_data = {"tag": {"id": 1}}
        response = self.session.post(url='https://%s/cgi-bin/tags/delete?access_token=%s' % (self.HOSTS, token_id),
                                     json=post_data)
        actula_result = response.json()['errcode']
        print(response.json())
        self.assertEqual(actula_result, 45058, 'case07 验证test_delect_tag接口删除0/1/2默认标签时是否正常处理')

if __name__ == '__main__':
    unittest.main(verbosity=2)