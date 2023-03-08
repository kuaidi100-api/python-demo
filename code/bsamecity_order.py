import json
import time
from bsamecity_common import do_request


def main():
    method = 'order'
    param = {
        "kuaidicom": "shunfengtongcheng",
        "lbsType": 2,
        "recManName": "顺丰同城",
        "recManMobile": "12345678910",
        "recManProvince": "北京市",
        "recManCity": "北京市",
        "recManDistrict": "海淀区",
        "recManAddr": "学清嘉创大厦A座15层",
        "recManLat": "40.014838",
        "recManLng": "116.352569",
        "sendManName": "测试",
        "sendManMobile": "12345678910",
        "sendManProvince": "北京",
        "sendManCity": "北京市",
        "sendManDistrict": "海淀区",
        "sendManAddr": "清华大学",
        "sendManLat": "40.002436",
        "sendManLng": "116.326582",
        "weight": "1",
        "remark": "测试下单",
        "volume": "",
        "salt": "",
        "callbackUrl": "http://www.baidu.com",
        "orderType": 0,
        "expectPickupTime": "",
        "expectFinishTime": "",
        "insurance": "",
        "price": "0",
        "goods": [
            {
                "name": "外卖",
                "type": "食品",
                "count": 0,
            }
        ]
    }
    t = str(int(round(time.time() * 1000)))
    return do_request(method, t, json.dumps(param))


if __name__ == '__main__':
    print(main())