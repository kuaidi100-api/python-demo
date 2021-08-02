# coding = utf-8
import json

import requests


class KuaiDi100:
    def __init__(self):
        self.key = ''  # TODO 客户授权key
        self.url = 'https://poll.kuaidi100.com/poll'  # 请求地址

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
                'resultv2': '1',  # 添加此字段表示开通行政区域解析功能。0：关闭（默认），1：开通行政区域解析功能
                'autoCom': '0',  # 添加此字段且将此值设为1，则表示开始智能判断单号所属公司的功能，开启后，company字段可为空,即只传运单号（number字段），我方收到后会根据单号判断出其所属的快递公司（即company字段）。建议只有在无法知道单号对应的快递公司（即company的值）的情况下才开启此功能
                'interCom': '0',  # 添加此字段且将此值设为1，则表示开启国际版，开启后，若订阅的单号（即number字段）属于国际单号，会返回出发国与目的国两个国家的跟踪信息，本功能暂时只支持邮政体系（国际类的邮政小包、EMS）内的快递公司，若单号我方识别为非国际单，即使添加本字段，也不会返回destResult元素组
                'departureCountry': '',  # 出发国家编码，interCom=1的国际单号最好提供该值
                'departureCom': '',  # 出发国家快递公司的编码，interCom=1的国际单号最好提供该值
                'destinationCountry': '',  # 目的国家编码，interCom=1的国际单号最好提供该值
                'destinationCom': '',  # 目的国家快递公司的编码，interCom=1的国际单号最好提供该值
                'phone': phone
            }
        }

        req_params = {
            'schema': 'json',  # 查询公司编号
            'param': json.dumps(param)  # 参数数据
        }

        return requests.post(self.url, req_params).text  # 发送请求


result = KuaiDi100().submit('yuantong', 'YT9693083639795', '', '江门市', '深圳市')
print(result)
