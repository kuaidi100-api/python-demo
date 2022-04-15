# coding = utf-8
"""
电子面单HTML
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
    url = 'http://poll.kuaidi100.com/eorderapi.do'  # 请求地址
    method = 'getElecOrder'

    param = {
        "partnerId": "",
        "partnerKey": "",
        "net": "",
        "kuaidicom": "zhaijisong",
        "recMan": {
            "name": "张三",
            "mobile": "138000138000",
            "printAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园B10",
            "company": ""
        },
        "sendMan": {
            "name": "李四",
            "mobile": "138000138000",
            "printAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园",
            "company": ""
        },
        "cargo": "发票",
        "count": "1",
        "weight": "0.5",
        "payType": "SHIPPER",
        "expType": "标准快递",
        "remark": "",
        "valinsPay": "",
        "collection": "",
        "needChild": "0",
        "needBack": "0",
        "orderId": "2147895476",
        "needTemplate": "1",
        "salt": "",
        "op": "0",
        "pollCallBackUrl": "",
        "resultv2": "0"
    }
    t = str(int(round(time.time() * 1000)))
    text = do_request(url, key, secret, method, t, json.dumps(param))
    print(text)
    result = json.loads(text)
    if result['result']:
        template_url = result['data'][0]['templateurl'][0]
        print(template_url)
