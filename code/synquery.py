# coding = utf-8
# 授权信息可通过链接查看：https://api.kuaidi100.com/manager/page/myinfo/enterprise

import hashlib
import json

import requests

key = ''  # 客户授权key
customer = ''  # 查询公司编号
param = {
    'com': 'yunda',  # 查询的快递公司的编码，一律用小写字母
    'num': '3950055201640',  # 查询的快递单号，单号的最大长度是32个字符
    'phone': '',  # 收件人或寄件人的手机号或固话（也可以填写后四位，如果是固话，请不要上传分机号）
    'from': '',  # 出发地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，请尽量提供
    'to': '',  # 目的地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，且到达目的地后会加大监控频率，请尽量提供
    'resultv2': '1',  # 添加此字段表示开通行政区域解析功能。0：关闭（默认），1：开通行政区域解析功能，2：开通行政解析功能并且返回出发、目的及当前城市信息
    'show': '0',  # 返回数据格式。0：json（默认），1：xml，2：html，3：text
    'order': 'desc'  # 返回结果排序方式。desc：降序（默认），asc：升序
}

pjson = json.dumps(param)  # 转json字符串

postdata = {
    'customer': customer,  # 查询公司编号
    'param': pjson  # 参数数据
}

# 签名加密， 用于验证身份， 按param + key + customer 的顺序进行MD5加密（注意加密后字符串要转大写）， 不需要“+”号
str = pjson + key + customer
md = hashlib.md5()
md.update(str.encode())
sign = md.hexdigest().upper()
postdata['sign'] = sign  # 加密签名

url = 'http://poll.kuaidi100.com/poll/query.do'  # 实时查询请求地址

result = requests.post(url, postdata)  # 发送请求
print(result.text)  # 返回数据
