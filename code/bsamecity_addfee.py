import json
import time
from bsamecity_common import do_request

def main():
    method = 'addfee'
    param = {
        "orderId": "100213",
        "remark": "",
        "taskId": "0E1536182BAE416080AC3C5DE6896F03",
        "tips": "10"
    }
    t = str(int(round(time.time() * 1000)))
    return do_request(method, t, json.dumps(param))


if __name__ == '__main__':
    print(main())