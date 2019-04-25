# import sys
# from urllib import request
#
# def download(url,fname):
#
#     r = request.urlopen(url)
#     with open(fname,'wb') as fobj:
#         while True:
#             data=r.read(1024)
#             if not data:
#                 break
#             fobj.write(data)
#
# if __name__ == '__main__':
#     download(sys.argv[1] , sys.argv[2])


####---获取一个网页代码
# from urllib import request
#
# respone = request.urlopen('http://www.baidu.com')
#                 # 向指定的url发送请求，并返回服务器响应的类文件对象
# print(respone.read())
#                 # 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串

####---修改请求头
# import urllib.request
#
# request = urllib.request.Request("http://www.baidu.com")
#                 # url 作为Request()方法的参数，构造并返回一个Request对象
# response = urllib.request.urlopen(request)
#                 # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
#
# html = response.read()
# print(html)

###查看请求信息将会变成:
# GET http://www.baidu.com/ HTTP/1.1
# Accept-Encoding: identity
# Host: www.baidu.com           #请求资源的主机变www.baidu.com
# User-Agent: Python-urllib/3.7
# Connection: close

##---爬取一个网站的所有图片,按原名命名--自己写的
# from urllib import request
# import re
# import os
#
# def ydm(fname):
#     # yurl = input('请输入网址:')
#     r = request.urlopen('http://www.tmooc.cn')
#
#     with open(fname,'wb') as fobj:
#         while True:                     #非文本用while,文本文件用for循环遍历
#             data = r.read(1024)         #与读取文件类似
#             if not data:
#                 break
#             fobj.write(data)
#     tpurl(fname)
#
# def tpurl(fname):
#
#     pngurl_list=[]
#     cpatt = re.compile('http:.*\.(png|jpg)')
#     # url = r'http://[.\w/-]+\.(jpg|png|jpeg|gif)' [. \w / -] +
#
#     with open(fname) as fobj:
#         for line in fobj:
#             m = cpatt.search(line)
#             if m:
#                 pngurl_list.append(m.group())
#     # print(pngurl_list)
#
#     hqtp(pngurl_list)
#
# def hqtp(pngurl_list):
#     img_dir = '/root/桌面/teduimg'
#
#     if not os.path.exists(img_dir):
#         os.mkdir(img_dir)
#     for i in pngurl_list:
#         pngname = os.path.split(i)
#         # print(pngname)
#         img_file= os.path.join(img_dir,pngname[-1])
#         # print(img_file)
#
#         print(i)
#         r = request.urlopen(i)
#         with open(img_file,'wb') as fobj:
#             while True:
#                 data=r.read(1024)
#                 if not data:
#                     break
#                 fobj.write(data)
#
# if __name__ == '__main__':
#     fname = '/root/桌面/tedu.txt'
#     ydm(fname)

# import os
# fname = 'http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo2.png'
# a = os.path.basename(fname)
# print(a)

##---爬取一个网站的所有图片,按原名命名--老师写day04-download.py---待补充注释

# from  urllib import request
# import re
# import os
#
#
# def downlod(url,fname):
#
#     r = request.urlopen(url)
#     with open(fname,'wb') as fobj:
#         while True:
#             data = r.read(1024)
#             if not data:
#                 break
#             fobj.write(data)
#
# def get_patt(fname,patt,encoding='utf8'):
#     cpatt = re.compile(patt)                #编译正则
#     patt_list = []
#
#     with open(fname,encoding=encoding) as fobj:
#         for lin in fobj:
#             m = cpatt.search(lin)
#             if m:
#                 patt_list.append(m.group())
#     return patt_list    #返回获取的图片列表给img_urls
#
# if __name__ == '__main__':
#     fname = '/root/桌面/download.html'
#     url = 'http://www.163.com'
#     downlod(url,fname)
#
#     img_patt = 'http://[\w/.-]+\.(jpg|png|jpeg|gif)'
#     img_urls = get_patt(fname,img_patt,'gbk')           #'gbk'为解码方式
#     print(img_urls)
#
#     img_dir = '/root/桌面/163'
#     if not os.path.exists(img_dir):
#         os.mkdir(img_dir)
#     for i in img_urls:
#         img_name = i.split('/')[-1]
#         img_name = os.path.join(img_dir,img_name)
#         downlod(i,img_name)


###########-urllib.error模块

# from urllib import request,error
#
# url1 = 'http://127.0.0.1/abcd'      #设置了不存在的网页
# url2 = 'http://127.0.0.1/ban'       #设置了没权限的网页
#
# try:
#     r1 = request.urlopen(url1)
#
# except error.HTTPError as e:   #把异常捕获后起名给变量e
#     print('错误:' , e)          #输出异常报错的内容, 报404 输出为:错误: HTTP Error 404: Not Found
#
# try:
#     r2 = request.urlopen(url2)
# except error.HTTPError as e:
#     print('错误' , e)           #输出异常报错的内容, 报403


########--request.quote函数
# from urllib import request
# url =  'http://www.sogou.com/web?query=复联4'
# # request.urlopen(url)      ##报错，汉字不是URL允许的字符
# a = request.quote('复联4')  #将汉子编码
# print(a)                    #输出编码值:%E5%A4%8D%E8%81%944
#
# url =  'http://www.sogou.com/web?query=' + request.quote('复联4')
# print(url)                  #输出可用url:http://www.sogou.com/web?query=%E5%A4%8D%E8%81%944
# request.quote(url)
#
#











