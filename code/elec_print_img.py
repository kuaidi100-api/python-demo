# coding = utf-8
"""
电子面单图片
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
    url = 'https://poll.kuaidi100.com/printapi/printtask.do'  # 请求地址
    method = 'getPrintImg'

    param = {
        "type": "10",
        "partnerId": "",
        "partnerKey": "",
        "net": "",
        "kuaidicom": "zhaijisong",
        "recManName": "张三",
        "recManMobile": "13842569988",
        "recManPrintAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园",
        "sendManName": "李四",
        "sendManMobile": "13842569988",
        "sendManPrintAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园B10",
        "tempid": "e41bbe3a3c764409a8562b2715f656b2",
        "cargo": "发票",
        "count": "1",
        "weight": "0.5",
        "payType": "SHIPPER",
        "expType": "标准快递",
        "remark": "",
        "collection": "",
        "needChild": "",
        "needBack": "",
        "orderId": "",
        "height": "100",
        "width": "75",
        "salt": "123456789",
        "op": "0",
        "pollCallBackUrl": "",
        "resultv2": "0"
    }
    t = str(int(round(time.time() * 1000)))
    text = do_request(url, key, secret, method, t, json.dumps(param))
    print(text)
    result = json.loads(text)
    if result['result']:
        img_base64 = json.loads(result['data']['imgBase64'])[0]
        print(img_base64)
