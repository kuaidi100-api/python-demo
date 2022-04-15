# -*- coding: utf-8 -*-
"""
快递单号回传及订单发货
"""

import hashlib
import json

import requests


def do_request(url, key, secret, param):
    md = hashlib.md5()
    md.update((param + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        'param': param,
        'sign': sign
    }
    return requests.post(url, payload).text


if __name__ == '__main__':
    key = ''  # TODO 客户授权key
    secret = ''  # TODO 秘钥
    url = 'https://api.kuaidi100.com/ent/logistics/send'  # 请求地址

    param = {
        "shopType": "******",
        "shopId": "******",
        "orderNum": "******",
        "kuaidiCom": "******",
        "kuaidiNum": "******"
    }
    result = do_request(url, key, secret, json.dumps(param))
    print(result)
