
import unittest
import requests
from common.config_utils import config
from common import api_info
from common.log_utils import logger


class TestGetTokenApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()
    def test_get_accesstoken_success(self):
        self._testMethodName = 'case01'
        self._testMethodDoc = '验证access_token接口是否正常'
        logger.info('case01 验证access_token接口是否正常 --开始执行--')
        response = api_info.get_access_token_api(self.session,self.HOSTS,
                                                 "wxb4f279bf92396ac6",
                                                 "e6d7e52c5babdd0941e2f4b1af400de4")
        result_code = response.status_code
        logger.info('case01 验证access_token接口是否正常 --执行结束--')
        self.assertEqual(result_code,200,'验证access_token接口是否正常')
'''
    def test_get_accesstoken_appid_error(self):
        self._testMethodName = 'case02'
        self._testMethodDoc = '验证appid错误时，get_access_token接口能否正常处理'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wxb4f279bf9221396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40013,'验证appid错误时，get_access_token接口能否正常处理')

    def test_get_accesstoken_AppSecret_error(self):
        self._testMethodName = 'case03'
        self._testMethodDoc = '验证AppSecret错误时，get_access_token接口能否正常处理'

        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40001,'验证AppSecret错误时，get_access_token接口能否正常处理')

    def test_get_accesstoken_grant_type_error(self):
        self._testMethodName = 'case04'
        self._testMethodDoc = '验证grant_type错误时，get_access_token接口能否正常处理'
        get_param_dict = {
            "grant_type": "client_creden12tial",
            "appid": "wxb4f279bf92396ac6",
            "secret": "e6d7e52c5babdd0941e2f4b1af400de4"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)
        response = self.session.get( url='https://%s/cgi-bin/token'%self.HOSTS,
                         params=get_param_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40002,'验证grant_type错误时，get_access_token接口能否正常处理')
'''

if __name__=='__main__':
    unittest.main()