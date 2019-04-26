###---编码
# data='中国'
# print(data.encode())   #转换成utf8的二进制形式 #输出：b'\xe4\xb8\xad\xe5\x9b\xbd'
# print(type(data))      #输出：<class 'str'>  数据类型为字符型
# # help(data.encode)    #可看到默认的编码方式是utf8
# data_1 = data.encode('gbk')     #转换成gbk的二进制形式,
# print(data_1)                   #输出：b'\xd6\xd0\xb9\xfa'
# print(type( data_1))            #输出<class 'bytes'> 数据类型是bytes(二进制)
# # print(data_1.decode())        #bdata是gbk编码，默认decode用的是utf8，所以报错
# print(data_1.decode('gbk'))     #指定采用gbk的方式解码  输出：中国

# from urllib import request
# url_1 = 'http://www.sogou.com/web?query=复联4'
# # request.urlopen(url_1)          #报错，汉子不是URL允许的字符
# print(request.quote('复联4'))     # 编码：输出：%E5%A4%8D%E8%81%944
# url_2 = 'http://www.sogou.com/web?query=' + request.quote('复联4') #真正的网址
# print(url_2)         #输出：http://www.sogou.com/web?query=%E5%A4%8D%E8%81%944
#
#############天气预报
# import urllib.request
# import json
# r = urllib.request.urlopen('http://www.weather.com.cn/data/sk/101230201.html')
# data_1 = r.read()
# data_2 = json.loads(data_1)   # 将json字符串转成字典
# print(data_2)   #输出：{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9'。。。。。。
# print(data_2['weatherinfo']['city'])        #输出：北京
# print(data_2['weatherinfo']['temp'])        #输出：27.9



######################---json
# import json
# data1 = {'str3':'xyz','str2':'efgh','str1':'abcd'}
# d1 = json.dumps(data1,sort_keys=True)
# print(d1)           #输出：{"str1": "abcd", "str2": "efgh", "str3": "xyz"}
#
# import json
# adict = {'name': 'tom', 'age': 20}      #原始数据
#
# jdata1 = json.dumps(adict)      # 将字典转换成json字符串
# print(jdata1)                   #输出:{"name": "tom", "age": 20}
#
# jdata2 = json.loads(jdata1)     # 将json字符串转成字典
# print(jdata2)                   #输出:{'name': 'tom', 'age': 20}


##################---request.get模块--要实验看看
# import requests
# r = requests.get('http://www.sogou.com')
# a = r.text
# print(a)

# r = requests.get('https://upload-images.jianshu.io/upload_images/14715425-24448b60df04d2eb.png')
# with open('/root/桌面/123.png', 'wb') as fobj:
#     fobj.write(r.content)


#####--查快递——


#'http://www.kuaidi100.com/query?type=%s&postid=%s'
url = 'http://www.kuaidi100.com/query'
params = {'type': 'youzhengguonei', 'postid': '9893442769997'}
r = requests.get(url,params=params)
result = r.json()
print(result)

# a = '123'
# print(eval(a))
# print(type(eval(a))) 






















































