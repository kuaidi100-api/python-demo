# coding = utf-8
import hashlib
import json
import time

import requests

# 国际地址解析接口
def main():
    url = "https://api.kuaidi100.com/internationalAddress/resolution"  # 请求地址
    key = ""            #客户授权key
    secret = ""         #秘钥
    param = {
        #国家或地区二字码
        "code": "US",
        #地址
        "address": "84 Alford Rd, Great Barrington, MA 01230, USA",
        #语言码
        "language": "zh"
    }

    t = str(int(round(time.time() * 1000)))

    md = hashlib.md5()
    md.update((str(json.dumps(param)) + t + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        't': t,
        'param': json.dumps(param),
        'sign': sign
    }
    return requests.post(url = url, data = payload).content.decode("utf-8")


if __name__ == '__main__':
    print(main())