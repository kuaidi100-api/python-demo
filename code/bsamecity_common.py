import hashlib

import requests

BSAMECITY_URL = "https://api.kuaidi100.com/bsamecity/order"

def do_request(method, t, param):
    key = ''            #客户授权key
    secret = ''         #秘钥
    url = BSAMECITY_URL #请求地址
    md = hashlib.md5()
    md.update((param + t + key + secret).encode())
    sign = md.hexdigest().upper()
    payload = {
        'key': key,
        'method': method,
        't': t,
        'param': param,
        'sign': sign
    }
    return requests.post(url, payload).content.decode("utf-8")