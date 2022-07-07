# -*- coding: utf-8 -*-
"""
电子面单v2，下单接口
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
    method = 'order'

    param = {
        "partnerId": "123456",
        "partnerKey": "",
        "code": "",
        "kuaidicom": "zhaijisong",
        "recMan": {
            "name": "张三",
            "mobile": "13888888888",
            "printAddr": "广东深圳市南山区金蝶软件园",
            "company": ""
        },
        "sendMan": {
            "name": "李四",
            "mobile": "13888888888",
            "printAddr": "广东深圳市南山区金蝶软件园",
            "company": ""
        },
        "cargo": "test",
        "tempId": "60f6c17c7c223700131d8bc3",
        "childTempId": "61bff9efc66fb00013a1b168",
        "backTempId": "61bffa26c66fb00013a1b16c",
        "payType": "SHIPPER",
        "expType": "标准快递",
        "remark": "测试下单,请勿发货",
        "collection": "0",
        "needChild": "0",
        "needBack": "0",
        "count": 1,
        "printType": "CLOUD",
        "siid": "KX100*******",
        "needDesensitization": True,
        "needLogo": True,
        "needOcr": False
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)
