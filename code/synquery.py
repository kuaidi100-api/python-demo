# coding = utf-8
import hashlib
import json

import requests


class KuaiDi100:
    def __init__(self):
        self.key = ''  # TODO 客户授权key
        self.customer = ''  # TODO 查询公司编号
        self.url = 'https://poll.kuaidi100.com/poll/query.do'  # 请求地址

    def track(self, com, num, phone, ship_from, ship_to):
        """
        物流轨迹实时查询
        :param com: 查询的快递公司的编码，一律用小写字母
        :param num: 查询的快递单号，单号的最大长度是32个字符
        :param phone: 收件人或寄件人的手机号或固话（也可以填写后四位，如果是固话，请不要上传分机号）
        :param ship_from: 出发地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，请尽量提供
        :param ship_to: 目的地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，且到达目的地后会加大监控频率，请尽量提供
        :return: requests.Response.text
        """
        param = {
            'com': com,
            'num': num,
            'phone': phone,
            'from': ship_from,
            'to': ship_to,
            'resultv2': '1',  # 添加此字段表示开通行政区域解析功能。0：关闭（默认），1：开通行政区域解析功能，2：开通行政解析功能并且返回出发、目的及当前城市信息
            'show': '0',  # 返回数据格式。0：json（默认），1：xml，2：html，3：text
            'order': 'desc'  # 返回结果排序方式。desc：降序（默认），asc：升序
        }
        param_str = json.dumps(param)  # 转json字符串

        # 签名加密， 用于验证身份， 按param + key + customer 的顺序进行MD5加密（注意加密后字符串要转大写）， 不需要“+”号
        temp_sign = param_str + self.key + self.customer
        md = hashlib.md5()
        md.update(temp_sign.encode())
        sign = md.hexdigest().upper()
        request_data = {'customer': self.customer, 'param': param_str, 'sign': sign}
        return requests.post(self.url, request_data).text  # 发送请求


result = KuaiDi100().track('yuantong', 'YT9693083639795', '', '广东省江门市', '广东省深圳市')
print(result)
