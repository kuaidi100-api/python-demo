import hashlib
import json
import time

import requests

# 运单附件查询接口
def main():
    url = "https://api.kuaidi100.com/label/order"  # 请求地址
    key = ""            #客户授权key
    secret = ""         #秘钥
    method = "backOrder"
    param = {
        #快递公司编码
        "kuaidicom": "shunfeng",
        #快递单号
        "kuaidinum": "SF1234567",
        #附件类型
        "imgType": 1,
        #电子面单账号
        "partnerId": "123456789",
        #电子面单密码
        "partnerKey": "123456789",
        #寄件人手机号
        "phone": "13088888888"

    }
    t = str(int(round(time.time() * 1000)))

    md = hashlib.md5()
    md.update((str(json.dumps(param)) + t + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        'method': method,
        't': t,
        'param': json.dumps(param),
        'sign': sign
    }
    return requests.post(url = url, data = payload).content.decode("utf-8")


if __name__ == '__main__':
    print(main())