# coding = utf-8
"""
通过快递公司或网点、菜鸟与淘宝提供的电子面单账号，对已经提交过的面单但没有寄发的面单号进行取消，快速回收面单
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
    url = 'https://poll.kuaidi100.com/eorderapi.do'  # 请求地址
    method = 'cancel'
    param = {
        "partnerId": "",
        "partnerKey": "",
        "partnerSecret": "",
        "partnerName": "",
        "net": "",
        "code": "",
        "kuaidicom": "******",
        "kuaidinum": "******",
        "orderId": "",
        "reason": ""
    }

    t = str(int(round(time.time() * 1000)))
    text = do_request(url, key, secret, method, t, json.dumps(param))
    print(text)
