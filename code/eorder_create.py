# -*- coding: utf-8 -*-
"""
电子面单v2，复打接口
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
    url = 'https://api.kuaidi100.com/label/order'  # 请求地址
    method = 'printOld'

    param = {
        "taskId": "xxxx",
        "siid": "KX100*******"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)
