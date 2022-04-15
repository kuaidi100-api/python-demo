# coding = utf-8
"""
通过第三方授权获取月结账号授权码
"""
import hashlib
import json
import time

import requests


def do_request(url, key, secret, t, param):
    md = hashlib.md5()
    md.update((param + t + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        't': t,
        'param': param,
        'sign': sign
    }
    return requests.post(url, payload).text


if __name__ == '__main__':
    key = ''  # TODO 客户授权key
    secret = ''  # TODO 秘钥
    url = 'https://poll.kuaidi100.com/printapi/authThird.do'  # 请求地址
    param = {
        "net": "cainiao",
        "partnerId": "",
        "callBackUrl": "",
        "view": ""
    }

    t = str(int(round(time.time() * 1000)))
    text = do_request(url, key, secret, t, json.dumps(param))
    print(text)
    result = json.loads(text)
    if result['data']:
        print(result['data']['url'])
