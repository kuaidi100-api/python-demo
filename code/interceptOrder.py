import hashlib
import json
import time

import requests

# 订单拦截接口
def main():
    url = "https://api.kuaidi100.com/label/order"  # 请求地址
    key = ""            #客户授权key
    secret = ""         #秘钥
    method = "interceptOrder"
    param = {
        "callbackUrl":"http://api.kuaidi100.com/test/callback",
        "interceptPayType":"THIRDPARTY",
        "interceptType":"MODIFY_ADDR",
        "kuaidicom":"jtexpress",
        "kuaidinum":"JT12345678",
        "orderId":"123456789",
        "orderRole":"1",
        "partnerId":"12345678",
        "partnerKey":"12345678",
        "reason":"测试拦截",
        "recManInfo":{
            "mobile":"130******66",
            "name":"张三",
            "printAddr":"广东省深圳市南山区粤海街道科技南十二路金蝶软件园"
        },
        "salt":"kuaidi1000api@salt"
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