# -*- coding: utf-8 -*-
"""
商家寄件，选择快递公司进行下单
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
    method = 'bOrder'

    param = {
        "kuaidicom": "yuantong",
        "recManName": "王超",
        "recManMobile": "13842569988",
        "recManPrintAddr": "广东深圳市深圳市南山区科技南十二路2号金蝶软件园",
        "sendManName": "王大",
        "sendManMobile": "13842569988",
        "sendManPrintAddr": "广东省广州市华景软件园",
        "cargo": "文件",
        "callBackUrl": "http: //www.baidu.com",
        "payment": "SHIPPER",
        "serviceType": "标准快递",
        "weight": "1",
        "remark": "",
        "salt": "",
        "dayType": "",
        "pickupStartTime": "",
        "pickupEndTime": "",
        "passwordSigning": "Y",
        "valinsPay": "",
        "op": "0",
        "pollCallBackUrl": "",
        "resultv2": "0"
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, method, t, json.dumps(param))
    print(result)  # {"data":{"kuaidinum":"YT2213099035201","orderId":"20066771","attach":null,"taskId":"9FC293CA417E431F33046E64F4C4EC20"},"message":"提交成功","result":true,"returnCode":"200"}
