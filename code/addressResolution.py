# coding = utf-8
import hashlib
import json
import time

import requests

# 地址解析接口
def main():
    url = "https://api.kuaidi100.com/address/resolution"  # 请求地址
    key = ""            #客户授权key
    secret = ""         #秘钥
    param = {
            "content":"张三广东省深圳市南山区粤海街道科技南十二路金蝶软件园13088888888"
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