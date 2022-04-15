# -*- coding: utf-8 -*-
"""
同城配送，通过第三方授权获取商家账号授权码
"""
import hashlib
import json
import time

import requests


def do_request(url, key, secret, method, t, param):
    md = hashlib.md5()
    md.update((param + t + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        'method': method,
        't': t,
        'param': param,
        'sign': sign
    }
    return requests.post(url, payload).text


if __name__ == '__main__':
    key = ''  # TODO 客户授权key
    secret = ''  # TODO 秘钥
    url = 'https://order.kuaidi100.com/sameCity/order'  # 请求地址
    method = 'auth'

    param = {
        "com": "shansong",
        "storeId": "******",
        "callbackUrl": "http://www.baidu.com"
    }
    t = str(int(round(time.time() * 1000)))
    response = do_request(url, key, secret, method, t, json.dumps(param))
    print(response)
    result = json.loads(response)
    if result['data']:
        print(result['data']['url'])
