import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse


def send_msg():
    timestamp = str(round(time.time() * 1000))
    secret = 'SECb158a238083ecfc93927cd1dddf99cb3286971e0caa02887666566452eb28deb'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print(timestamp)
    print(sign)
    url = 'https://oapi.dingtalk.com/robot/send?access_token' \
          '=58f5af713a6c03ef77434213ababb1824430ac4f5060fd4ebdec8e49c51f774b&timestamp={}&sign={}'.format(timestamp,
                                                                                                          sign)

    print(url)
    headers = {
        'Content-Type': 'application/json'
    }
    param = {
        "msgtype": "text",
        "text": {
            "content": "您的自动化测试报告已生成："
        }
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(param))
    print(resp.text)


if __name__ == '__main__':
    send_msg()
