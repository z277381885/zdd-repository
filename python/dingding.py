
#!/usr/bin/env python3

import json
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            # "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['13973169942']         # 特殊提醒要查看的人,就是@某人一下
    url = 'https://oapi.dingtalk.com/robot/send?access_token=0f8f9b33b9d3b5e09082306d6ae56deee996718e5d1acd339906af2b3dd0b1aa'
        #url地址来源与钉钉机器人管理复制webhook地址而来
    print(send_msg(url, reminders, msg))


