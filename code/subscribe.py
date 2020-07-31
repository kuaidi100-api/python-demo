# coding = utf-8
# 授权信息可通过链接查看：https://api.kuaidi100.com/manager/page/myinfo/enterprise

import json

import requests

key = ''  # 客户授权key

parameters = {
    'callbackurl': 'http://www.xxxxx.com/callback?orderId=123',  # 回调接口的地址。如果需要在推送信息回传自己业务参数，可以在回调地址URL后面拼接上去，如示例中的orderId
    'salt': '',  # 签名用随机字符串。32位自定义字符串。添加该参数，则推送的时候会增加sign给贵司校验消息的可靠性
    'resultv2': '1',  # 添加此字段表示开通行政区域解析功能。0：关闭（默认），1：开通行政区域解析功能
    'autoCom': '0',  # 添加此字段且将此值设为1，则表示开始智能判断单号所属公司的功能，开启后，company字段可为空,即只传运单号（number字段），我方收到后会根据单号判断出其所属的快递公司（即company字段）。建议只有在无法知道单号对应的快递公司（即company的值）的情况下才开启此功能
    'interCom': '0',  # 添加此字段且将此值设为1，则表示开启国际版，开启后，若订阅的单号（即number字段）属于国际单号，会返回出发国与目的国两个国家的跟踪信息，本功能暂时只支持邮政体系（国际类的邮政小包、EMS）内的快递公司，若单号我方识别为非国际单，即使添加本字段，也不会返回destResult元素组
    'departureCountry': '',  # 出发国家编码，interCom=1的国际单号最好提供该值
    'departureCom': '',  # 出发国家快递公司的编码，interCom=1的国际单号最好提供该值
    'destinationCountry': '',  # 目的国家编码，interCom=1的国际单号最好提供该值
    'destinationCom': '',  # 目的国家快递公司的编码，interCom=1的国际单号最好提供该值
    'phone': ''  # 收件人或寄件人的手机号或固话（也可以填写后四位，如果是固话，请不要上传分机号）
}

param = {
    'company': 'yunda',  # 快递公司编码
    'number': '3950055201640',  # 快递单号
    'from': '',  # 出发地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，请尽量提供
    'to': '',  # 目的地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，且到达目的地后会加大监控频率，请尽量提供
    'key': key,  # 客户授权key
    'parameters': parameters
}

pjson = json.dumps(param)  # 转json字符串

postdata = {
    'schema': 'json',  # 查询公司编号
    'param': pjson  # 参数数据
}

url = 'https://poll.kuaidi100.com/poll'  # 订阅请求地址

result = requests.post(url, postdata)  # 发送请求
print(result.text)  # 返回数据
