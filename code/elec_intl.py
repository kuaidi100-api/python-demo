# -*- coding: utf-8 -*-
"""
国际电子面单
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
    url = 'http://api.kuaidi100.com/sendAssistant/order/apiCall'  # 请求地址

    param = {
        "partnerId": "",
        "partnerName": "",
        "partnerKey": "",
        "partnerSecret": "",
        "code": "",
        "kuaidicom": "fedex",
        "sendMan": {
            "name": "Kaka",
            "mobile": "13500000000",
            "addr": "Kingdee Software Park",
            "district": "Hi-tech Park,Nanshang District",
            "province": "",
            "company": "QIAN HAI BAI DI",
            "countryCode": "CN",
            "city": "SHEN ZHEN",
            "zipcode": "518057",
            "tel": "0755-5890123",
            "email": "12344655@qq.com",
            "vatNum": "IOSS23249923",
            "eoriNum": "IOSS23249923",
            "iossNum": "IOSS23249923"
        },
        "recMan": {
            "name": "Cindy Martinez / Ana Luz Medina",
            "mobile": "(86)13560312000",
            "addr": "Apoquindo 4001, of. 501. Las Condes",
            "district": "Santiago, Chile",
            "province": "",
            "company": "Lamaignere Chile S.A.",
            "countryCode": "CL",
            "city": "Santiago",
            "zipcode": "7550000",
            "tel": " +56 (9) 1242355",
            "email": "12344699@qq.com",
            "vatNum": "IOSS23249923",
            "eoriNum": "IOSS23249923",
            "iossNum": "IOSS23249923"
        },
        "cargo": "test don't ship",
        "count": "1",
        "weight": "0.1",
        "expType": "FedEx International Priority®",
        "remark": "just a test demo",
        "packageInfos": [
            {
                "height": "10",
                "width": "20",
                "length": "11",
                "weight": "0.1",
                "packageReference": "just a user remark"
            }
        ],
        "exportInfos": [
            {
                "netWeight": 0.1,
                "grossWeight": 0.1,
                "manufacturingCountryCode": "CN",
                "unitPrice": "10.0",
                "quantity": 1.0,
                "quantityUnitOfMeasurement": "PCS",
                "desc": "test",
                "importCommodityCode": "6109100021",
                "exportCommodityCode": "6109100021",
                "numberOfPieces": 1
            }
        ],
        "customsValue": "10.0",
        "tradeTerm": "DAP",
        "needInvoice": False,
        "invoiceInfo": {
            "date": "2021-08-12",
            "number": "15462412",
            "type": None,
            "title": "test",
            "signature": "base64Str",
            "pltEnable": True
        },
        "dutiesPaymentType": {
            "paymentType": "DDU",
            "account": "60*****43"
        },
        "freightPaymentType": {
            "paymentType": "SHIPPER",
            "account": "60*****43"
        },
        "customsClearance": {
            "purpose": "",
            "document": True
        }
    }
    t = str(int(round(time.time() * 1000)))
    result = do_request(url, key, secret, t, json.dumps(param))
    print(result)
