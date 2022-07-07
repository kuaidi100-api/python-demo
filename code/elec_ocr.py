# -*- coding: utf-8 -*-
"""
电子面单OCR识别
"""
import base64
import json

import requests


def do_request(url, key, param):
    payload = {
        'key': key,
        'param': param
    }
    return requests.post(url, payload).text


if __name__ == '__main__':
    key = 'xxxx'  # TODO 客户授权key
    url = 'http://api.kuaidi100.com/elec/detocr'  # 请求地址
    b64 = base64.b64encode(open(r'xxx.jpeg', 'rb').read()).decode()
    param = {
        'enableTilt': True,
        'image': b64,
        'imageUrl': None,
        'pdfUrl': None,
        'include': ['barcode', 'qrcode', 'receiver', 'sender']  # 取值范围：['barcode', 'qrcode', 'receiver', 'sender', 'bulkpen', 'expType']，不传或者None则默认为 ['barcode', 'receiver', 'sender']
    }
    response = do_request(url, key, json.dumps(param))
    print(response)
