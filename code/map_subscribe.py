# coding = utf-8
import json

import requests


class KuaiDi100:
    def __init__(self):
        self.key = ''  # TODO 客户授权key
        self.url = 'https://poll.kuaidi100.com/pollmap'  # 请求地址

    def submit(self, com, num, phone, ship_from, ship_to):
        """
        物流轨迹订阅
        :param com: 快递公司编码
        :param num: 快递单号
        :param phone: 收件人或寄件人的手机号或固话（也可以填写后四位，如果是固话，请不要上传分机号）
        :param ship_from: 出发地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，请尽量提供
        :param ship_to: 目的地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，且到达目的地后会加大监控频率，请尽量提供
        :return: requests.Response.text
        """
        param = {
            'company': com,
            'number': num,
            'from': ship_from,
            'to': ship_to,
            'key': self.key,
            'parameters': {
                'callbackurl': 'https://www.baidu.com/kd100/callback',  # 回调接口的地址。如果需要在推送信息回传自己业务参数，可以在回调地址URL后面拼接上去，例如：https://www.baidu.com/kd100/callback?orderId=123
                'salt': None,  # 签名用随机字符串。32位自定义字符串。添加该参数，则推送的时候会增加sign给贵司校验消息的可靠性
                'phone': phone,  # 收寄件人的移动电话号码（只能填写一个，顺丰速运和丰网速运必填，其他快递公司选填）
                'ordertime': '2022-02-21 10:19:21',  # 订单下单时间，格式: yyyy-MM-dd HH:mm:ss
                'resultv2': '6'
            }
        }

        req_params = {
            'schema': 'json',  # 查询公司编号
            'param': json.dumps(param)  # 参数数据
        }

        return requests.post(self.url, req_params).text  # 发送请求


result = KuaiDi100().submit('yuantong', 'YT9693083639795', '', '江门市', '深圳市')
print(result)
