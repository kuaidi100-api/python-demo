# coding = utf-8
"""
获取授权账户绑定网点信息以及账户可用单量
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
        'method': method,
        'key': key,
        't': t,
        'param': param,
        'sign': sign
    }
    return requests.post(url, payload).text


if __name__ == '__main__':
    key = ''  # TODO 客户授权key
    secret = ''  # TODO 秘钥
    url = 'http://poll.kuaidi100.com/eorderapi.do'  # 请求地址
    method = 'getThirdInfo'
    param = {
        "partnerId": "******",
        "partnerKey": "******",
        "net": "******",
        "com": None
    }

    t = str(int(round(time.time() * 1000)))
    text = do_request(url, key, secret, method, t, json.dumps(param))
    print(text)
