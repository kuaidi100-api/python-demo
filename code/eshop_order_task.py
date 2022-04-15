# -*- coding: utf-8 -*-
"""
提交订单获取任务
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
    url = 'https://api.kuaidi100.com/ent/order/task'  # 请求地址

    param = {
        "shopType": "TAOBAO",
        "shopId": "******",
        "orderStatus": "UNSHIP",
        "updateAtMin": "2022-02-22 13:00:00",
        "updateAtMax": "2022-02-22 13:30:00",
        "callbackUrl": "******",
        "salt": None
    }
    result = do_request(url, key, secret, json.dumps(param))
    print(result)
