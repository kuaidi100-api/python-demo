# coding = utf-8
import hashlib
import json
import time

import requests

key = ''  # 客户授权key
secret = ''  # 电子面单secret
siid = ''  # 打印机设备码
param = {
    "tempid": "137977264104148992",
    "siid": siid,
    "callBackUrl": "http://www.baidu.com/fhd/callback",
    "petName": "kd100",
    "recName": "小百",
    "recPhone": "10086",
    "payTime": "2021-01-15 15:40:55",
    "expressName": "德邦快递",
    "printTime": "2021-01-15 15:41:30",
    "printCount": "1",
    "address": "广东省深圳市南山区金蝶软件园",
    "total": "21", 
    "remark": "购物小票作为购物凭证，请妥善保管，您有任何疑问，请咨询服务热线 123456798",
    "img0": {
        "type": "code_128",
        "content": "887921256577",
        "width": 350,
        "height": 100
    },
    "tab0": [
        {
            "prodName": "热敏纸",
            "count": "5",
            "specs": "76*130",
            "unitPrice": "30",
            "price": "150"
        },
        {
            "prodName": "热敏纸",
            "count": "10",
            "specs": "100*180",
            "unitPrice": "50",
            "price": "500"
        },
        {
            "prodName": "续打纸",
            "count": "5",
            "specs": "",
            "unitPrice": "40",
            "price": "200"
        },
        {
            "prodName": "云打印机",
            "count": "1",
            "specs": "二代",
            "unitPrice": "499",
            "price": "499"
        }
    ]
}

settings = {
    "pageWidth": 100,
    "pageHeight": 180,
    "margins": {
        "top": 5,
        "bottom": 5,
        "left": 5,
        "right": 5
    }
}

param_json = json.dumps(param)
timestamp = str(time.time())
md = hashlib.md5()
tmp = param_json + timestamp + key + secret
md.update(tmp.encode())
sign = md.hexdigest().upper()

req_params = {
    'method': 'billparcels',
    'key': key,
    't': timestamp,
    'sign': sign,
    'param': param_json,
    'settings': json.dumps(settings)
}
url = 'https://poll.kuaidi100.com/print/billparcels.do'  # 请求地址

print(req_params)

result = requests.post(url, req_params)  # 发送请求
print(result.text)  # 返回数据
