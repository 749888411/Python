python通过http发送post请求接口数据

import json
import time
import requests

url = 'http://127.0.0.1:8080/add/serialnumber'
headers = {'Accept': "application/json", 'Content-Type': 'application/json', 'Authorization': 'Basic cxxxxXXXxxXXXxXXx'}

a = {'869405030990008': ['宝山路001号', 'TEST', 'TEST-ABC-NB01'], '869405030980009': ['宝山路002号', 'TEST', 'TEST-ABC-NB02'],
     '86940503099000a': ['宝山路00a号', 'TEST', 'TEST-ABC-NB01']}
for key, value in a.items():
    data = {"serialNumber": key, "protocol": "NB-IOT", "groupName": "DM.TEST.TESTADD",
            "additionalParams": {'adaptationLayerName': 'TEST_NB', 'tag': 'TEST-ABC-NB-V1',
                                 "deployaddr": value[0], 'manufacturer': value[1], 'model': value[2], }}
    data = json.dumps(data)
    res = requests.post(url, data=data, headers=headers, auth=('test', 'Test#001'))
    print(key)
    print(res.content)
    time.sleep(1)


# coding:utf-8
import requests

url = "https://passport.cnblogs.com/user/signin"
# 接口地址
# 消息头数据
headers = {'Connection': 'keep-alive',
           'Content-Length': '123',
           'Cache-Control': 'max-age=0',
           'Origin': 'https://passport.csdn.net',
           'Upgrade-Insecure-Requests': '1',
           'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Referer': 'https://passport.csdn.net/account/login?from=http://www.csdn.net',
           'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cookie': '省略', }
payload = {'username': '**', 'password': '**', 'lt': '**', 'execution': 'e1s1', '_eventId': 'submit', }
# verify = False 忽略SSH 验证
r = requests.post(url, json=payload, headers=headers, verify=False)
json2 = r.json()
print(json2)
