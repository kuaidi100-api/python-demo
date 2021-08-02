# coding = utf-8

import hashlib

import requests


class KuaiDi100:
    def __init__(self):
        self.key = ''  # TODO 客户授权key
        self.userid = ''  # TODO 查询公司编号
        md = hashlib.md5()
        md.update((self.key + self.userid).encode())
        self.sign = md.hexdigest().upper()
        self.url = 'https://apisms.kuaidi100.com/sms/send.do'  # 接口地址，或者 http://apisms.kuaidi100.com:9502/sms/send.do

    def send_sms(self, seller, phone, tid, sms_content, order_id):
        """
        短信发送
        :param seller: 商户名称签名；最好用简称，该字段信息会在短信标签处显示。不要超过5个字符
        :param phone: 接收短信手机号
        :param tid: 短信模板ID
        :param sms_content: 短信模板替换内容
        :param order_id: 外部订单号：当该短信发送模板有回调地址时，外部订单号会返回给调用者，方便用户更新数据
        :return: requests.Response.text
        """
        req_params = {
            'sign': self.sign,  # 加密签名信息：MD5(key + userid)；加密后字符串转大写
            'userid': self.userid,  # 我方分配给贵司的的短信接口用户ID，点击查看账号信息
            'seller': seller,  # 商户名称签名；最好用简称，该字段信息会在短信标签处显示。不要超过5个字符
            'phone': phone,  # 接收短信手机号
            'tid': tid,  # 短信模板ID
            'content': sms_content,  # 短信模板替换内容
            'outorder': order_id,  # 外部订单号：当该短信发送模板有回调地址时，外部订单号会返回给调用者，方便用户更新数据
            # 'callback': 'https//www.baidu.com/kd100/callback'  # 回调地址：如果客户在发送短信时填写该参数，将按照这个参数回调短信发送状态；如果为空，将按照模板配置的地址回调短信发送状态；如果两个参数都不填写，将不会回调通知状态
        }

        return requests.post(self.url, req_params).text  # 发送请求


content = {  # 短信模板替换内容
    "接收人姓名": "小百",
    "公司名": "快递100",
    "快递单号": "154893238584",
    "url": "https://www.kuaidi100.com"
}
result = KuaiDi100().send_sms('快递100', '13800138000', '11', content, '123456789')
print(result)
