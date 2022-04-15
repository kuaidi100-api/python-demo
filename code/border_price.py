# -*- coding: utf-8 -*-
"""
商家寄件，查看从出发地到目的地的价格
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
    method = 'price'

    param = {
        "kuaidicom": "yuantong",
        "sendManPrintAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园",
        "recManPrintAddr": "广东省广州市华景软件园",
        "weight": "1",
        "serviceType": "标准快递"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)  # {"data":{"serviceType":"标准快递","defPrice":"10.0","overPrice":"0","kuaidiCom":"yuantong","defFirstPrice":"10.0","defOverPrice":"0","price":"10.0","firstPrice":"10.0"},"message":"成功","result":true,"returnCode":"200"}
