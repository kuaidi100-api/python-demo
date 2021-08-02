# coding = utf-8
import hashlib
import json
import time

import requests


class KuaiDi100:
    def __init__(self):
        self.key = ''  # TODO 客户授权key
        self.secret = ''  # TODO 电子面单secret
        self.url = 'https://poll.kuaidi100.com/print/billparcels.do'  # 请求地址

    def submit(self, param, settings):
        """
        发货单打印
        :param param: 模板配置信息和自定义参数信息
        :param settings: 纸张配置信息
        :return: requests.Response.text
        """
        timestamp = str(time.time())
        md = hashlib.md5()
        param_str = json.dumps(param)
        temp_sign = param_str + timestamp + self.key + self.secret
        md.update(temp_sign.encode())
        sign = md.hexdigest().upper()
        req_params = {
            'method': 'billparcels',
            'key': self.key,
            't': timestamp,
            'sign': sign,
            'param': param_str,
            'settings': json.dumps(settings)
        }
        return requests.post(self.url, req_params).text  # 发送请求


param = {
    "tempid": "xxxx",  # 模板编码，通过管理后台的打印发货单模板配置信息获取
    "siid": "xxxx",  # 打印设备码，通过打印机输出的设备码进行获取
    "callBackUrl": "https://www.baidu.com/fhd/callback",  # 打印状态对调地址
    "petName": "kd100",  # 自定义参数
    "recName": "小百",  # 自定义参数
    "recPhone": "10086",  # 自定义参数
    "payTime": "2021-01-15 15:40:55",  # 自定义参数
    "expressName": "德邦快递",  # 自定义参数
    "printTime": "2021-01-15 15:41:30",  # 自定义参数
    "printCount": "1",  # 自定义参数
    "address": "广东省深圳市南山区金蝶软件园",  # 自定义参数
    "total": "21", "remark": "购物小票作为购物凭证，请妥善保管，您有任何疑问，请咨询服务热线 123456798",  # 自定义参数
    "img0": {  # 图片参数，多图片时用img0,img1,img2等追加
        "type": "code_128",
        "content": "887921256577",
        "width": 350,
        "height": 100
    },
    "tab0": [  # 表格参数，多表格时用tab0，tab1，tab2等追加对象
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
    "pageWidth": 100,  # 纸张宽，单位mm，默认值：100
    "pageHeight": 180,  # 纸张高，单位mm ，续打纸张时，该字段设置为null或空串
    "margins": {  # 边距
        "top": 5,  # 上边距，单位：mm，默认：0
        "bottom": 5,  # 下边距，单位：mm，默认：0
        "left": 5,  # 左边距，单位：mm，默认：0
        "right": 5  # 右边距，单位：mm，默认：0
    }
}

result = KuaiDi100().submit(param, settings)
print(result)
