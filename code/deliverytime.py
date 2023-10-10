import hashlib
import json
import time

import requests


def main():
    url = "https://api.kuaidi100.com/label/order"  # 请求地址
    key = ""            #客户授权key
    secret = ""         #秘钥
    method = "time"
    param = {
        #快递公司编码
        "kuaidicom": "jd",
        #出发地（地址需包含3级及以上），例如：广东深圳南山区
        "from": "广东省广州市白云区",
        #目的地（地址需包含3级及以上），例如：北京海淀区
        "to": "广东省深圳市南山区",
        #下单时间，格式要求yyyy-MM-dd HH:mm:ss, 例如：2023-10-12 10:00:00
        "orderTime": "2023-10-12 10:00:00",
        #产品类型
        "expType": "特惠送"
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