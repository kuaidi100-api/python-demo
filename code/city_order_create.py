# -*- coding: utf-8 -*-
"""
同城配送，选择快递公司进行下单
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
    method = 'order'

    param = {
        "com": "kfw",
        "recManName": "测试",
        "recManMobile": "13542651579",
        "recManPrintAddr": "深圳市南山区伟易达大夏",
        "sendManName": "小张",
        "sendManMobile": "13542651579",
        "sendManPrintAddr": "深圳市南山区高新南地铁站b口",
        "serviceType": "火锅",
        "weight": 1.00,
        "remark": "测试订单，待会取消",
        "salt": "123",
        "callBackUrl": "http://www.baiud.com",
        "orderType": 0,
        "pickupTime": "",
        "orderSourceNo": "168168168",
        "orderSourceType": "美团",
        "storeId": "106396",
        "additionFee": 1000,
        "partnerId": "******",
        "partnerKey": "******"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)
