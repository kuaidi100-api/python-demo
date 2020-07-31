# coding = utf-8
# 授权信息可通过链接查看：https://api.kuaidi100.com/manager/page/myinfo/enterprise

import hashlib

import requests

key = ''  # 客户授权key
userid = ''  # 查询公司编号
md = hashlib.md5()
md.update((key + userid).encode())
sign = md.hexdigest().upper()
postdata = {
    'sign': sign,  # 加密签名信息：MD5(key + userid)；加密后字符串转大写
    'userid': userid,  # 我方分配给贵司的的短信接口用户ID，点击查看账号信息
    'seller': '',  # 商户名称签名；最好用简称，该字段信息会在短信标签处显示。不要超过5个字符
    'phone': '',  # 接收短信手机号
    'tid': '',  # 短信模板ID
    'content': {  # 短信模板替换内容
        "接收人姓名": "小百",
        "公司名": "快递100",
        "快递单号": "154893238584",
        "url": "http://www.kuaidi100.com"
    },
    'outorder': '',  # 外部订单号：当该短信发送模板有回调地址时，外部订单号会返回给调用者，方便用户更新数据
    'callback': ''  # 回调地址：如果客户在发送短信时填写该参数，将按照这个参数回调短信发送状态；如果为空，将按照模板配置的地址回调短信发送状态；如果两个参数都不填写，将不会回调通知状态
}

url = 'http://apisms.kuaidi100.com:9502/sms/send.do'  # 短信发送接口地址

result = requests.post(url, postdata)  # 发送请求
print(result.text)  # 返回数据
