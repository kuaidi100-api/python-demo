# coding = utf-8

import requests


class KuaiDi100:
    def __init__(self):
        self.key = ''  # TODO 客户授权key
        self.url = 'https://www.kuaidi100.com/autonumber/auto'  # 请求地址

    def auto_number(self, num):
        """
        智能单号识别
        :param num: 快递单号
        :return: requests.Response.text
        """
        req_params = {'key': self.key, 'num': num}
        return requests.post(self.url, req_params).text  # 发送请求


result = KuaiDi100().auto_number('YT9693083639795')
print(result)
