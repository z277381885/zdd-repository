# import requests
# r = requests.get('http://www.sogou.com')
# a = r.text
# print(a)

# r = requests.get('https://upload-images.jianshu.io/upload_images/14715425-24448b60df04d2eb.png')
# with open('/root/桌面/123.png', 'wb') as fobj:
#     fobj.write(r.content)


####---json
# import json
# adict = {'name': 'tom', 'age': 20}
#
# jdata1 = json.dumps(adict)      # 将字典转换成json字符串
# print(jdata1)                   #输出:{"name": "tom", "age": 20}
#
# jdata2 = json.loads(jdata1)     # 将json字符串转成字典
# print(jdata2)                   #输出:{'name': 'tom', 'age': 20}

import urllib.request
import email.parser
# r = urllib.request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
# data = r.read()
#
# import json
# print(json.loads(data))



