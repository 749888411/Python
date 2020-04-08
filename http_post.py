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
