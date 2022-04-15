# coding = utf-8
"""
电子面单打印
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
    siid = ''  # TODO 打印机设备码
    url = 'https://poll.kuaidi100.com/printapi/printtask.do'  # 请求地址
    method = 'eOrder'

    param = {
        "type": "10",
        "partnerId": "",
        "partnerKey": "",
        "net": "",
        "kuaidicom": "zhaijisong",
        "recMan": {
            "name": "张三",
            "mobile": "13751866787",
            "printAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园B10",
            "company": ""
        },
        "sendMan": {
            "name": "李四",
            "mobile": "13751866787",
            "printAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园",
            "company": ""
        },
        "cargo": "发票",
        "count": "1",
        "weight": "0.5",
        "payType": "SHIPPER",
        "expType": "标准快递",
        "remark": "",
        "tempid": "e41bbe3a3c764409a8562b2715f656b2",
        "siid": siid,
        "valinsPay": "",
        "collection": "",
        "needChild": "0",
        "needBack": "0",
        "orderId": "2147895476",
        "height": "100",
        "width": "75",
        "callBackUrl": "",
        "salt": "",
        "op": "0",
        "pollCallBackUrl": "",
        "resultv2": "0"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)
