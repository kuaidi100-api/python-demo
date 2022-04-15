# -*- coding: utf-8 -*-
"""
商家寄件，对下完单进行取消操作
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
    url = 'https://poll.kuaidi100.com/order/borderapi.do'  # 请求地址
    method = 'cancel'

    param = {
        "taskId": "9FC293CA417E431F33046E64F4C4EC20",
        "orderId": "20066771",
        "cancelMsg": "内部测试单"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)  # {"data":{},"message":"取消成功","result":true,"returnCode":"200"}
