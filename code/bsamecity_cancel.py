import json
import time
from bsamecity_common import do_request

def main():
    method = 'cancel'
    param = {
        "orderId": "100241",
        "cancelMsgType": 1,
        "cancelMsg": "测试寄件",
        "taskId": "DE49A5C45B0845328CE0AE8EF9951EC5"
    }
    t = str(int(round(time.time() * 1000)))
    return do_request(method, t, json.dumps(param))


if __name__ == '__main__':
    print(main())