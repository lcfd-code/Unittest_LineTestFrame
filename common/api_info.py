#!/usr/bin/python
# -*- coding:utf-8 -*-


import requests
import json
from common.log_utils import logger
from requests.exceptions import ReadTimeout,ConnectionError,RequestException


def get_access_token_api(session,hosts,appid,secret,grant_type='client_credential'): # 如果是带有默认值的放最后面
    logger.info('调用获取access_token接口')
    get_param_dict = {
        "grant_type": grant_type,
        "appid": appid,
        "secret": secret
    }
    response = None
    try:
        response = session.get(url='https://%s/cgi-bin/token'%hosts,
                                params=get_param_dict)
    except RequestException as e:
        logger.error('调用获取access_token接口失败，原因是%s'%e.__str__())
    return response

def get_access_token_value(session, hosts): # 登录时候处理关联用的,调用过多的可以写死参数在这
    response = get_access_token_api(session, hosts, 'wxb4f279bf92396ac6', 'e6d7e52c5babdd0941e2f4b1af400de4')
    return response.json()['access_token']

def test_create_tag(session,hosts,token_id,post_data):
    logger.info('调用test_create_tag接口')
    str_data = json.dumps(post_data, ensure_ascii=False)  # 处理json传输数据编码不对的情况
    response = session.post(url=' https://%s/cgi-bin/tags/create?access_token=%s'%(hosts,token_id),
                                 data=str_data.encode('utf-8'))
    return response

