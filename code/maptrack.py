# coding = utf-8
import hashlib
import json

import requests

key = ''  # 客户授权key
customer = ''  # 客户账号

param = {
    'com': 'yuantong',
    'num': 'YT5149923777495',
    'phone': '',
    'from': '安徽芜湖',
    'to': '深圳市南山区',
    'phone': '',
    'show': '0',
    'order': "desc",
    'orderTime': '2020-12-16 12:59:59'
}

param_json = json.dumps(param)

md = hashlib.md5()
tmp = param_json + key + customer
md.update(tmp.encode())
sign = md.hexdigest().upper()

req_params = {
    'customer': customer,
    'sign': sign,
    'param': param_json
}

url = 'https://poll.kuaidi100.com/poll/maptrack.do'  # 请求地址

print(req_params)

result = requests.post(url, req_params)  # 发送请求
print(result.text)  # 返回数据
result_json = json.loads(result.text)
print(result_json['trailUrl'])  # 轨迹地图链接
