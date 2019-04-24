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

##---爬取一个网站的所有图片,按原名命名
from urllib import request
import re
import os

def ydm(fname):
    # yurl = input('请输入网址:')
    r = request.urlopen('http://www.tmooc.cn')

    with open(fname,'wb') as fobj:
        while True:
            data = r.read(1024)         #与读取文件类似
            if not data:
                break
            fobj.write(data)
    tpurl(fname)

def tpurl(fname):

    pngurl_list=[]
    cpatt = re.compile('http:.*\.(png|jpg)')
    # url = r'http://[.\w/-]+\.(jpg|png|jpeg|gif)'

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                pngurl_list.append(m.group())
    # print(pngurl_list)

    hqtp(pngurl_list)

def hqtp(pngurl_list):
    img_dir = '/root/桌面/teduimg'

    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    for i in pngurl_list:
        pngname = os.path.split(i)
        # print(pngname)
        img_file= os.path.join(img_dir,pngname[-1])
        # print(img_file)

        print(i)
        r = request.urlopen(i)
        with open(img_file,'wb') as fobj:
            while True:
                data=r.read(1024)
                if not data:
                    break
                fobj.write(data)

if __name__ == '__main__':
    fname = '/root/桌面/tedu.txt'
    ydm(fname)

# import os
# fname = 'http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo2.png'
# a = os.path.basename(fname)
# print(a)




###compile函数:对正则表达式模式进行编译,返回一个正则表达式对象
##不是必须要用这种方式,但是在大量匹配的情况下,可以提升效率
# i = re.search('f..' , 'seafood')
# print(i.group())		#输出:foo,如下也可以用compile函数

# patt = re.compile('http:.*\.png')            #模式先编译,可提升效率,建议做法
# i = patt.search('<img class="default-logo" src="http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo.png"/>')
# 			#编译后的对象也有search(返回第一个匹配)/findall(返回列表)等方法
# print(i.group())
#
# print()
#
# patt = re.compile('"http:.*\.png"')            #模式先编译,可提升效率,建议做法
# i = patt.findall('<img class="default-logo" src="http://cdn.tmooc.cn/tmooc-web/css/img/tmooc-logo.png"/>')
# 			#编译后的对象也有search(返回第一个匹配)/findall(返回列表)等方法
# print(i)


