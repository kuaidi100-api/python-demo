# -*- coding: utf-8 -*-
"""
获取店铺授权超链
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
    url = 'https://api.kuaidi100.com/ent/shop/authorize'  # 请求地址

    param = {
        "shopType": "TAOBAO",
        "callbackUrl": "https://www.baidu.com/kd100/callback",
        "salt": None
    }
    result = do_request(url, key, secret, json.dumps(param))
    print(result)
