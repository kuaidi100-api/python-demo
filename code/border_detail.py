# -*- coding: utf-8 -*-
"""
商家寄件，订单详情查询接口
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
    url = 'https://order.kuaidi100.com/order/borderapi.do'  # 请求地址
    method = 'detail'

    param = {
        "taskId": "xxxx"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)
