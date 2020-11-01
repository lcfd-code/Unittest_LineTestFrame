#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import unittest
from common.config_utils import config

class TestUpdateTagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()


    def test_update_tag(self):
        self._testMethodName = 'case09'
        self._testMethodDoc = '验证test_update_tag接口是否正常'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wxb4f279bf92396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)
        token_id = response.json()['access_token']
        # print(token_id)
        post_data = {   "tag" : {     "id" : 100,     "name" : "广东人3"   } }
        response = self.session.post(url='https://%s/cgi-bin/tags/update?access_token=%s'%(self.HOSTS,token_id),
                                    json=post_data)
        actula_result = response.json()['errmsg']
        print(response.json())
        self.assertEqual(actula_result,"ok", 'case9 验证test_update_tag接口是否正常')

    def test_update_tag_error(self):
        self._testMethodName = 'case10'
        self._testMethodDoc = '验证test_update_tag_error接口是否正常'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wxb4f279bf92396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)
        token_id = response.json()['access_token']
        # print(token_id)
        post_data = {   "tag" : {     "id" : 100,     "name" : "嘎嘎嘎"   } }
        response = self.session.post(url='https://%s/cgi-bin/tags/update?access_token=%s' % (self.HOSTS, token_id),
                                     json=post_data)
        actula_result = response.json()['errcode']
        print(response.json())
        self.assertEqual(actula_result, 45157, 'case10 验证test_update_tag接口长度超过30个字节时是否正常处理')

if __name__ == '__main__':
    unittest.main(verbosity=2)