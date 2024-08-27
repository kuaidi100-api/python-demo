# coding = utf-8
import hashlib
import json
import time

import requests

# 地址解析接口
def main():
    url = "https://api.kuaidi100.com/label/order"  # 请求地址
    key = ""            #客户授权key
    secret = ""         #秘钥
    param = {
        "sendAddr": "深圳南山区金蝶软件园",
        "recAddr": "北京海淀区",
        "kuaidicom": "jd",
        "weight": "12"
    }
    t = str(int(round(time.time() * 1000)))

    md = hashlib.md5()
    md.update((str(json.dumps(param)) + t + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        't': t,
        'method':'price',
        'param': json.dumps(param),
        'sign': sign
    }
    return requests.post(url = url, data = payload).content.decode("utf-8")


if __name__ == '__main__':
    print(main())