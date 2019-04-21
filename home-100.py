###01-hello world#############
# if 3 > 0:
#     print('ok')
# x = 3 ; y = 4
# print('x')
# print(x)
# print('y')
# print(y)
# print(x + y)
###02-print###############################
# name = 'zdd'
# print(name)
# print('hello world!')
# print('hello','world')  #逗号自动添加默认的分隔符：空格
# print('zhu'+'dongdong') #+号表示字符拼接
# print(name +'dongdong') #+号表示字符拼接
# print('zhu','world',sep='***')  #逗号默认分隔符是空格，可用sep指定分隔符
# print('$' * 50)   #表示$字符重复50遍
# print('how are you?',end='')        #取消回车,每个print默认有个回车输入
# print('how are you?',)
###03-基本运算##############################
# # ###运算符可以分为：算术运算符、比较运算符和逻辑运算符。
# # ###优先级是：算术运算符>比较运算符>逻辑运算符。
# # ###不过呢，开始没背下来优先级，最好使用括号。
# # ###这样不用背，也增加了代码的可读性。
# print(5 / 2)   #结果2.5
# print(5 // 2)   #舍弃余数，只留商
# print(5 % 2)    #取余
# print(2 ** 2)   #2的2次方
# print(2 ** 3)   #2的3次方
# print(5 > 3)    #返回True
# print(3 > 5)    #返回False
# print(5 > 3 > 2) #返回True 支持连续比较
# print(5 > 3  and  3 > 1) #返回True与上相同
# print(5 >3  and 2 > 3 )  #返回False
# print(not 20 > 10)       #返回False. 判断20 不大于0，小于等于0
####04-input########################################
# number = input('请输入内容：')  #获取键盘输入
# print(number)                   #输出number变量
# print(type(number))             #返回str：number获取的数据是字符型
# number_1 = int(number)          #将字符转换成数字类型
# print(type(number_1))           #返回int: number获取的数据是数字类型
# ########
# number = input('请输入内容：')  #获取键盘输入的字符
# print(number + 10)              #报错，字符是不能做数字运算
# ######
# number = input('请输入内容：')  #获取键盘输入的字符
# print(int(number) + 10 )        #获取的字符转换成数字类型后再运算，输入1 返回11
# ########
# number = input('请输入内容：')  #获取键盘输入的字符
# print(number + str(10))         #将10转换成字符，然后进行字符拼接，输入2 返回210
####05-输入输出基础练习##################################
# username = input('username: ')
# print('welcome:', username)             #输入zdd,输出：welcome: zdd
# print('welcome:', username ,sep='$$')   #输入zdd,输出：welcome:$$zdd
# print('welcome:   ' + username)         #输入zdd,输出：welcome:   zdd
###06-字符串的使用基础###################################
# a1 = 'tom\'s pet is a cat'           #单引号内有单引号需要转义
# a2 = "tom's pet is a cat"            #双引号内有单引号不需要转义
# a3 = "tom said:\"hello world!\""    #双引号内有双引号需要转义
# a4 = 'tom said:"hello worid"'       #单引号内有双引号不需要转义
# print(a1,a2,sep='***')        #显示：tom's pet is a cat***tom's pet is a cat
# print(a3,a4,sep='***')        #显示：tom said:"hello world!"***tom said:"hello worid"
# words = '''
# hello
# world
# zdd'''       #三引号（三个单引号或者三个双引号）保持输入格式，允许输入多行字符串
# print(words)
###截取字符串#####
# py_str = 'python'
# str_cd = len(py_str)    #截取后赋值给一个参数
# print(len(py_str))      #输出：6  len 截取字符串长度
# print(str_cd)           #输出：6
# print('python'[0])      #输出:p  输出python字符串的第一个字符  p
# print(py_str[1])        #输出:y  输出变量字符串的第二个字符  y
# print(py_str[5])        #输出第六个字符  n
# print(py_str[-1])       #输出最后一个个字符  p
# print(py_str[2:4])      #输出第三个到第五个之前，不包括第五个  th
# print(py_str[2:])       #输出第三个到最后一个     thon
# print(py_str[:4])       #输出第一个到第五个之前，不包括第五个  pyth
# print(py_str[:])        #输出全部  python
# print(py_str[::2])      #从第一个开始，每隔2个去一个  pto
# print(py_str[1::2])     #从第二个开始，每隔2个取一个  yhn
# print(py_str[::-1])     #开始未写步长为负,表示从又往左取，nohtyp
# print(py_str + ' is good')  #返回python is good，，简单拼接
# print(py_str  * 3)       #返回 pythonpythonpython 重复三遍
# print( 't' in py_str)   #返回True，，判断t是否在py_str变量定义的字符串中
# print('th' in py_str)   #返回True，，判断tn是否在。。。。
# print('to' in py_str)   #返回False,,  判断to是否在、、、、
# print('to' not in py_str)   #返回True，，判断to 是否不在py_str变量中
###07-列表基础##########################################################
# alist = [10,20,30,'b0b','alice',[1,2,3]]
# print(len(alist))
# print(alist[-1])
# print(alist[-1][-1])    #取出alist列表中最后一项[1,2,3]中的最后一项
# print(alist[-1][-3])
# print([1,2,3,][-1])
# print(alist[-2][2])
# print(alist[3:5])
# print(10 in alist)      #true
# print('b' in alist[3])  #true
# print('b' in alist)     #false
# print(100 not in alist) #true
# print(alist)
# alist[1] = 100
# print(alist)
# alist.append(200)           #向列表中追加一项
# print(alist)
# alist[-2].pop(-1)         #删除列表中的列表[1,2,3]的最后一项3
# print(alist)
# alist.remove(20)            #删除20这个元素
# print(alist)
###08-元组基础############################################
####元组与列表基本上是一样的，只是元组不可变，列表可变
# atuple = (10,20,30,'bob','alice',[1,2,3])
# print(len(atuple))
# print(10 in atuple)
# print(atuple[2])
# print(atuple[3:5])
#### atuple[-1] = 100  # 错误，元组是不可变的
###09-字典基础##############################################
####字典是key-value(键－值）对形式的，没有顺序，通过键取出值
# adict = {'name':'bob','age':'23'}
# print(len(adict))           #2
# print('bob' in adict)       #false
# ####print('bob' in adict[key])  #错误
# print('name' in adict)      #true
# adict['email']='bob@tedu.cn'        #字典中没有key,则添加新项目
# print(adict)        #{'name': 'bob', 'age': '23', 'email': 'bob@tedu.cn'}
# adict['age'] = 25                   #字典中有的key,则更新修改对应的value
# print(adict)        #{'name': 'bob', 'age': 25, 'email': 'bob@tedu.cn'}
############################################################################
# info=["zhangsan","man",{"age":123}]
# username,sex,age=info             #等于是直接返回值中拿到变量
# print(username)
# print(sex)
# print(age)
###10-基本判断###############################################
###单个的数据也可作为判断条件。
###任何值为0的数字、空对象都是False，任何非0数字、非空对象都是True。
# if 3 > 0:
#     print('yes')
#
# if 3 < 0:
#     print('yes')
# else:
#     print('no')         #结果是no
#
# if 10 in [10,20,30]:    #10在列表里为true
#     print('ok')
#
# if -0.0 :               #任何值为0的数字都是false
#     print('yes')
# else:
#     print('no')         #结果是no
#
# if [1,2]:               #任何非空对象都是True
#     print('yes12')
#
# if '  ':                  #空格字符也也是字符,条件为True
#     print('yes')
# ####11-条件表达式,三元运算符#######################################
# a = 10
# b = 20
# if a < b:
#     smaller = a
# else:
#     smaller = b
# print(smaller)
#
# s = a if a < b else b       #和上面语句等价:如果a<b s就等于a 否则就等于b的值
# print(s)                    #输出:10
#
# m = a if a > b else b       #如果a>b m就等与a的值,否则就等于b的值
# print(m)                    #输出:20
######12-判断练习:用户名和密码是否正确##############################
# import  getpass
# username = input('username: ')
# password = input('password: ')
# # password = getpass.getpass('password: ')
# if username == 'root' and password == '123456':
#     print('yes')
# else:
#     print('no')
######13-猜数字:基础实现
# import random
# num = random.randint(1,10)
# ren = int(input('请输入一个数字: '))
# if ren > num:
#     print('大了')
# elif ren < num:
#     print('小了')
# else:
#     print('猜对了')
# print('结果是:%s' % num)
######14-成绩分类1############
# cj = int(input('请输入成绩:'))
# if cj > 90:
#     print('优秀')
# elif cj > 80:
#     print('好')
# elif cj > 70:
#     print('良')
# elif cj > 60:
#     print('及格')
# else:
#     print('冒搞手')
#####15成绩分类2##################
# def cjfl(cj):
#     if cj >= 90:
#         fl = '优秀'
#     elif 80 <= cj < 90:
#         fl = '好'
#     elif 70 <= cj < 90:
#         fl = '还行'
#     elif 60 <= cj < 70:
#         f1 = '及格'
#     else:
#         fl = '冒搞手哒'
#     return fl
# fs = int(input('请输入您的成绩：'))
# a = cjfl(fs)
# print(a)
#####16--石头剪刀布游戏###############
# import random
# all_cq = ['石头','剪刀','布']
# all_win = (['石头','剪刀'],['剪刀','布'],['布','石头'])
# c_jq = random.choice(all_cq)
# c_xz = '''0/石头
# 1/剪刀
# 2/布
# 请选择（0/1/2）'''
# c_ren1 = int(input(c_xz))
# c_ren2 = all_cq[c_ren1]
# if [c_ren2,c_jq] in all_win:
#     print('\033[31;1m你赢了\033[0m')
# elif c_ren2 == c_jq:
#     print('\033[32;1m平局\033[0m')
# else:
#     print('\033[31;1m你输了\033[0m')
# print('你出的是:%s  机器出的是:%s' % (c_ren2,c_jq))
#####18--猜数，直到猜对
# import random
# sz_sj = random.randint(1,100)
#
# while True:
#     sz_rc = int(input('请输入数字：'))
#     if sz_rc > sz_sj:
#         print('大了')
#     elif sz_rc < sz_sj:
#         print('小了')
#     else:
#         print('对了')
#         break
#####19--猜数字，五次机会#############
# import random
# sz_sj = random.randint(1,100)
# sz_cs = 0
# sz_d  = 0
# while sz_cs < 5:
#     sz_rc = int(input('请输入数字：'))
#     sz_cs += 1
#     if sz_rc > sz_sj:
#         print('大了')
#     elif sz_rc < sz_sj:
#         print('小了')
#     else:
#         print('对了')
#         break
# print('总共猜了:%s次' % sz_cs)
#####20-while循环，累加至100##############
# numb = 0
# cs   = 0
# while cs < 100:
#     cs += 1
#     numb = numb + cs
# print(numb)
######21-while-break
###--break是结束循环，break之后、循环体内代码不再执行。
######22-while-continue###
###--continue是跳过本次循环剩余部分，回到循环条件处。
##计算100以内偶数之和
# sz_sum = 0
# sz_counter = 0
# while sz_counter < 4:
#     sz_counter += 1
#     if sz_counter % 2 == 1:
#         continue          #凡是遇到基数就不执行下面的加法运算，跳到while判断位置
#     sz_sum = sz_sum + sz_counter
# print(sz_sum)
####23-for循环遍历数据对象
# astr = 'hello'
# alist = [10,20,30]
# atuple = ('zdd1','bob','tom','alice')
# adict = {'name':'john','age':23}
# for ch in astr:
#     print(ch)   #每行输出一个astr中的一个单词，
# for i in alist:
#     print(i)    #每行输出一个alist中的一个value
# for name in  atuple:
#     print(name)     #每行输出一个atuple中的一个名字
# for key in adict:
#     print('%s:%s' % (key,adict[key]))    #输出所有的键
####24-range 用法及数字累加#############
# print(range(10))            #输出range(0, 10)
# print(list(range(5)))       #输出[0, 1, 2, 3, 4]
# print(list(range(1,5)))     #输出[1, 2, 3, 4]
# print(list(range(1,5,2)))   #输出[1, 3] 从1开始，5结束，每隔一个输出一个，步长为2，不包括结束位5
# print(list(range(10,0)))    #输出[]
# print(list(range(10,0,-1))) #输出[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# #100以内的总和
# cont = 0
# a = 0
# for i in range(1,101):
#     cont += 1
#     a = a + cont
# print(a)
# ####25斐波那契数列
# a = [0,1]
# b = int(input('请输入数字个数'))
# for i in range(b-2):
#   a.append(a[-1] + a[-2])
# print(a)
#####26-九九乘法表
# cs = int(input('乘法表范围'))
# for i in range(1,cs+1):
#     for n in range(1,i+1):
#         print('%s*%s=%s ' % (i,n,i*n),end='')
#     print()
# # print(list(range(1,5)))
# # print(list(range(1,2)))
#####27-列表解析
# print([10 + 5 for  i  in  range(5)])   #输出：[15, 15, 15, 15, 15]，#10+5这个计算5次，for循环了5次
# print([10 + i for  i  in  range(5)])   #输出：[10, 11, 12, 13, 14]  #10+i,i来自于后面的for循环
# print([10 + i for  i  in  range(2,5)])  #输出：[12, 13, 14]  #10+i,i来自于后面的for循环
##通过if过滤，满足if条件的才参与10+i的运算
# print([10 + i for i in range(1,11) if i % 2 == 0]) #输出[12, 14, 16, 18, 20]
# print([10 + i for i in range(1,11) if i % 2 == 1])  #输出[11, 13, 15, 17, 19]
# print(['192.168.1.%s' %  i for i in range(1,10) if i > 8]) #输出['192.168.1.9']
# a =  ['192.168.1.%s' %  i for i in range(1,10) if i > 8]
# print(a)
#####三局两胜的石头剪刀布
# import random
# all = ['石头','剪刀','布']
# all_win = [['石头','剪刀'],['剪刀','布'],['布','石头']]
# xz='''
# 0/石头
# 1/剪刀
# 2/布
# 请选择数字出拳：'''
# cq_cs = 0
# rwin_cs = 0
# jqwin_cs =0
# cq_qk = []
# while  jqwin_cs < 3 and rwin_cs <3:
#     cq_cs += 1
#     cq_jq = random.choice(all)
#     id = int(input(xz))
#     cq_rc = all[id]
#     print('机器出的是：%s 你出的是：%s ' % (cq_jq, cq_rc))
#     if [cq_jq,cq_rc] in all_win:
#         print('所以是：\033[31;1m你赢了\033[0m')
#         rwin_cs += 1
#     elif cq_jq == cq_rc:
#         print('所以是：\033[32;1m平局\033[0m')
#     else:
#         print('所以是：\033[33;1m你输了\033[0m')
#         jqwin_cs += 1
# print('总共猜了%s局，你赢%s局，机器赢%s局' % (cq_cs,rwin_cs,jqwin_cs))
###29-文件对象基础操作---待续待续
##文件操作的三个步骤：打开、读写、关闭
# f = open('/tmp/passwd')  #默认以r方式打开
# data1 = f.read()         #read()默认把所有内容读取出来
# print(data1)
# data2 = f.read()        #前面一步已经将指针指向末尾了，再读就没有数据了
# print(data2)
# f.close()
#
# f.read(4)       #读取4个字节
# a = f.readline()      #读取一行，读到换行符结束
# b = f.readlines()      #把每一行数据读出来，放到列表中
#####30--拷贝文件1


#####31--拷贝文件2
# import sys
#
# def copy(src_fname,dst_fname):
#     src_fobj = open(src_fname,'rb')
#     dst_fobj = open(dst_fname,'wb')
#
#     while True:
#         data = src_fobj.read(4096)
#         if not data:
#             break
#         dst_fobj.write(data)
#     src_fobj.close()
#     dst_fobj.close()
#
# if __name__ == '__main__':
#     copy(sys.argv[1],sys.argv[2])
######32-位置参数
# import  sys
# print(sys.argv[1],sys.argv[2])      #sys.argv是sys模块里面的argv列表

# python3 position_args.py
# python3 position_args.py 10          #执行时带参数
# python3 position_args.py 10 bob       #执行时带两个参数

#####33-函数的应用，斐波那契数列
# import random,sys
#
# def gen_fib():
#     alist = [0, 1]
#     aint = int(input('请输入数字：'))
#     for i  in  range(aint - 2):
#         alist.append(alist[-1]+alist[-2])
#     return alist
# mylist=gen_fib()
# print(mylist)

####34-函数拷贝文件


####35-函数-九九乘法表
# def js():
#     cd = int(input('请输入长度'))
#     for i in range(cd+1):
#         for j in range(1,i+1):
#             print( '%s*%s=%s ' % (i,j,i*j),end='')
#         print()
# if __name__ == '__main__':
#     a = js()
####36-模块基础
# hi = 'hello world'
# def pstar(n=50):
#     print('*' * n)
#
# if __name__ == '__main__':
#     pstar()
#     pstar(20)
###37-生成随机密码
# import random
# import string
# import sys
#
# def passwd(n=8):
#     a = string.digits + string.ascii_letters
#     b = ''                                  #先定义个空字符
#     for i in range(n):
#         b += random.choice(a)
#
#     print(b)
#
# if __name__ == '__main__':
#     # a = sys.argv[1]
#     passwd()
#     passwd(4)

# print('%s' % i for i in range(8))
# a = list('%s' % i for i in range(7))
# b = list('%s' % i for i in range(1,7))
# print(a)
# print(b)
###38-序列对象方法

# print(list('hello'))     #将字符串转换成列表
# print(tuple('hello'))    #将字符串转换成元组
# print(str('hello'))      #字符串

# from random import randint
# # num_list = [randint(1, 100) for i in range(10)]
# # print(num_list)
# # print(max(num_list))
# # print(min(num_list))
#
# num_list = (randint(1, 100) for i in range(10))
# print(num_list)
#
# # print(max(num_list))
# # print(min(num_list))
#
# ages1 = (11,22,33,44,55)
# ages2 = [11,22,33,44,55]
# print(list(ages1))
# print(tuple(ages2))


###39-序列对象方法2
# alist = [10,'john','zdd']

# for ind in range (len(alist)):
#     print('%s ,%s' % (ind,alist[ind]))
#
# print(list((enumerate(alist))))    #输出[(0, 10), (1, 'john'), (2, 'zdd')]
#
# for item in enumerate(alist):
#     print('%s,%s' % (item[0],item[1]))
#
# for ind,val in enumerate(alist):      #常用
#     print('%s,%s' % (ind , val))
####以上都是输出:
# 0,10
# 1,john
# 2,zdd

# print(list((enumerate(alist))))
#[(0, 10), (1, 'john'), (2, 'zdd')]

# for ind,ch in enumerate(alist[1:]):
#     print(ind)
#     print(ch)
# ####以上输出:
# # 0
# # john
# # 1
# # zdd

# atuple = (96,97,40,75,58,34,69,29,66,90)
# # print(sorted(atuple))    #[29, 34, 40, 58, 66, 69, 75, 90, 96, 97]#从小到达排列,并转换为列表输出
# # print(sorted('hello'))     #['e', 'h', 'l', 'l', 'o']
#
# for i in reversed(atuple):
#     print(i,end=',')        #90,66,29,69,34,58,75,40,97,96,
#
# print(list(reversed(atuple))) #[90, 66, 29, 69, 34, 58, 75, 40, 97, 96]
#

#####40-字符串方法

# str = 'hello word!'
# print(str.capitalize())         #Hello word!
# print(str.title())
#
# print(str.center(15))           #居中
# print(str.center(15,'#'))       #输出:##hello word!##
# print(str.center(15),'#')       #普通输出:  hello word!   #
#
# print(str.ljust(15,'*'))        #字符串长度总共15字节,字符左对齐,少了右边用*补充
#                     #hello word!****
# print(str.rjust(15,'*'))        #字符串长度总共15字节,字符右对齐,少了左边用*补充
#                     #****hello word!
#
# print(str.count('l'))           #统计字符串中'l'出现的次数

# str = 'hello word!'
# print(str.endswith('!'))        #True   是否是'!'结尾
# print(str.endswith('a'))        #False
# print(str.startswith('h'))      #True   是否是'h'开头
# print(str.startswith('b'))      #False

# print(str.islower())               #True     判断是否全是小写
# print(str.isupper())               #False    判断是否全是大写
# print('adff'.islower())            #True   直接判断是否全是小写
# print('asdf'.isupper())            #False  直接判断是否全是大写

# print('hao123'.isdigit())           #False       判断是否全是数字
# print('123456'.isdigit())           #True        判断是否全是数字

# a_1 = '  hello\t '
# print(a_1)
# print(a_1.strip())                  #去掉两边空白字符,包括\t,\n
# print(a_1.lstrip())                 #去掉左边空白字符,包括\t,\n
# print(a_1.rstrip())                 #去掉右边空白字符,包括\t,\n
# print('  hello\t '.strip())                #可直接使用
##输出如下:
#   hello
# hello
# hello
#   hello
# hello

# a_2 = 'how are you?'
# print(a_2.split())
# a_3 = 'how_are_you'
# print(a_3.split('_'))
#
# a_4 = ['how', 'are', 'you']
# print('.'.join(a_4))            #输出:how.are.you
#############################################

###41-字符串格式化
# print('%s is %s years old' % ('zdd', 20))
# print('%s is %d years old' % ('zdd',21.5))  #21.5输出的是21,,%d是整数
# print('%s is %f years old' % ('zdd',21.5))  #21.5输出的是21.500000  %f是浮点数
# print('%s is %1.4f years old' % ('zdd',21.5))  #21.5输出的是21.50  %5.2f 5是宽度,2是小数位数

# print('97 is %c' % 97)  #转成字符输出:a
# print('98 is %c' % 98)  #转成字符输出:b
# print('99 is %c' % 99)  #转成字符输出:c
# # #输出:
# # 97 is a
# # 98 is b
# # 99 is c
#
# print('11 is %#o' % 11) # %#o表示有前缀的8进制
#
# print('%10s %5s' % ('name' , 'age'))   # 常用 右对齐字符宽度10 和 5
# print('%-10s %-5s' % ('name' , 'age'))   # 常用 左对齐字符宽度10 和 5
# # #输出
#       name   age
# name       age
#
# print('{} is {} years old'.format('bob',25) )
# print('{1} is {0} years old'.format(25,'bob'))
# print('{:<10}{:<8}'.format('name','age'))
# print('{:>10}{:>8}'.format('name','age'))
#输出
# bob is 25 years old
# bob is 25 years old
# name      age
#       name     age
#
####42-shutil模块常用方法
# import shutil
# with open('/test/passwd' , 'rb') as fobj:
#     with open('/test/passwd.txt' , 'wb') as dfobj:
#         shutil.copyfileobj(fobj,dfobj)

# shutil.copyfile('/test/passwd.txt' , '/test/123.txt')
# shutil.copy('/test/passwd.txt' , '/test/a/')
# shutil.copy2('/test/passwd' , '/test/a')
# shutil.move('/test/123.txt' , '/test/a' )
# shutil.copytree('/test' , '/test2/')
# shutil.rmtree('/test/a')
# shutil.copymode('/etc/shadow', '/test/123.txt')
# 将123.txt的元数据设置成与/etc/shadow一样
# 元数据使用stat /etc/shadow查看

# shutil.copystat('/etc/shadow', '/tmp/mima2.txt')
# shutil.chown('/tmp/mima2.txt', user='zhangsan', group='zhangsan')

###43-生成文本文件
# import os
# def get_fname():
#
#     while True:
#         fname = input('请输入文件名：')
#         if not os.path.exists(fname):
#             break
#         print('%s 文件已存在，请重新输入：' % fname)
#     return fname
#
# def get_content():
#     content = []
#     print('请输入内容，另起一行输入end结束')
#     while True:
#         a = input('>')
#         if a == 'end':
#             break
#         content.append(a)
#     return content
#
# def get_wfile(fname,content):
#     with open(fname ,'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     content = [line + '\n' for line in content]
#     get_wfile(fname,content)

###44-列表方法
# alist = [1,2,3,'bob',3,'alice',3]
# alist[0] = 10
# print(alist)
# print(alist[1:100])
# alist.append('zdd')
# print(alist)
# alist.remove(2)
# print(alist)
# print(alist.index(3,4))     #从alist[4]开始往后搜索，返回3的下标
# print(alist.insert(3,10))
# print(alist)
# blist = alist.copy()
# blist = alist
# print(blist)
# print(blist)
# print(alist.pop())
# print(alist)
# print(alist.pop(alist[2]))          #弹出是从后往前弹出
# print(alist)
# alist.pop()
# alist = [1,2,3,4,3,5,3]
# alist.sort()
# print(alist)
# alist.reverse()
# print(alist)
# print(alist.count(3))
# # alist.clear()
# print(alist)
# alist.append('new')
# print(alist)
# clist = [10,20,30]
# alist.extend(clist)         #将列表clist汇入alist列表
# print(alist)
# alist.extend('end')         #将'e' 'n' 'd'汇入到alist
# print(alist)
# alist.extend(['hello','world'])     #将['hello','world']汇入alist
# print(alist)

####45-检查合法字符
# import keyword
# import string
#
# def chckid(str):
#
#     if  keyword.iskeyword(str):
#         print('%s:this is keyword' % str)
#         exit()
#     if str[0] not in a:
#         print('%s 第一个字符不合法' % str)
#         exit()
#
#     for i in list(str):
#         # print(list(str))
#         # print(i)
#         if i not in b:
#             print('%s 中的 %s is not hefa' % (str, str[str.index(i)]) )
#
# if __name__ == '__main__':
#     a = string.ascii_letters + '_'
#     b = a + string.digits
#     print(a)
#     str = input('输入标识符：')
#     chckid(str)
####46-创建用户设置随机密码
import random
import string
import os
import subprocess

def pd(user):
    rc = subprocess.call('id %s' % user , shell=True)
    if rc:
        print('用户不存在')
        print(rc)
        rb = subprocess.call('useradd %s' % user , shell=True)
        if rb:
            print('%s 用户创建不成功' % user)
            exit()
        else:
            print('%s 用户创建成功' % user)
    else:
        print('无此用户')
        print(rc)
        exit()

    n = int(input('请输入要设置的密码长度：'))
    spasswd(n,user)

def spasswd(n, user):
    a =  string.digits + string.ascii_letters
    passwd = ''
    for i in range(n):
        passwd +=  random.choice(a)
    print(passwd)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd,user), shell=True)

if __name__ == '__main__':
    user = (input('please input user:'))
    pd(user)



###47--列表练习：模拟栈操作
# import sys
#
# list = []
#
# def rz():
#     print('rz')
#     itm = input('>').strip()
#     if itm:
#         list.append(itm)
# def cz():
#     print('cz')
#     if list:
#         print('弹出：%s' % list.pop())
# def cx():
#     print(list)
#
# def manu():
#     xz_lb='''0:入栈
# 1：出栈
# 2：查询
# 3：退出
# 请选择'''
#     while True:
#         xz = input(xz_lb).strip()
#         if xz not in  ['0','1','2','3']:
#             print('输入无效，请重新输入：')
#             continue
#         if xz == '3':
#             print('退出')
#             break
#         def_list = {'0':rz,'1':cz,'2':cx}
#         if xz in def_list:
#             def_list[xz]()
#
# if __name__ == '__main__':
#     manu()

###记账本
#! /usr/bin/env python
# import os,pickle,time
#
# def ruzhang(fname):
#     print('jz')
#     date = time.strftime('%Y-%m-%d')
#     rz_je = int(input('入账金额：'))
#     rz_sm = input('入账说明：')
#
#     with open(fname,'rb') as fobj:
#         data = pickle.load(fobj)
#         balance = data[-1][-2]+rz_je
#
#     line = [date,rz_je,0,balance,rz_sm]
#     data.append(line)
#
#     with open(fname,'wb') as fobj:
#         pickle.dump(data,fobj)
#
# def chuzhang(fname):
#     print('cz')
#     date = time.strftime('%Y-%m-%d')
#     cz_je = int(input('出账金额：'))
#     cz_sm = input('出账说明：')
#
#     with open(fname,'rb') as fobj:
#         data = pickle.load(fobj)
#         balance = data[-1][-2]-cz_je
#
#     line = [date,0,cz_je,balance,cz_sm]
#     data.append(line)
#
#     with open(fname,'wb') as fobj:
#         pickle.dump(data,fobj)
#
# def chaxun(fname):
#     print('cx')
#     print('%-10s%-8s%-8s%-10s%-20s' %  ('登记时间','入账金额','出账金额','余额','说明'))
#     with open(fname,'rb') as fobj:
#         data = pickle.load(fobj)
#     for line in data:
#         print('%-14s%-13s%-11s%-11s%-20s' % tuple(line))
#
#
# def view():
#     xz_1 = '''0:入账
# 1:出账
# 2:查询
# 3:退出
# 请选择（0/1/2）：'''
#     cmds = {'0':ruzhang,'1':chuzhang,'2':chaxun}
#     fname =  'jzb.txt'
#
#     if not os.path.exists(fname):
#         date_a = time.strftime('%Y-%m-%d')
#         data_a = [
#             [date_a,0,0,10000,'初始金额']
#         ]
#         with open(fname,'wb') as fobj:
#             pickle.dump(data_a,fobj)
#
#     while True:
#         xz_2 = input(xz_1).strip()
#         if xz_2 == '3':
#             print('选择退出')
#             exit()
#         if xz_2 not in ['0','1','2']:
#             print('无效输入')
#             continue
#         cmds[xz_2](fname)
#
# if __name__ == '__main__':
#     view()

#######################################################
###备份程序
# import os
# import time
# import tarfile
# import hashlib
# import pickle
# from check_md5 import check_md5
#
# def fullback(src,dst,md5):
#
#     fname = os.path.basename(src)
#     fname = '%s_full_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
#     fname = os.path.join(dst,fname)
#     print(fname)
#
#     tar = tarfile.open(fname,'w:gz')
#     tar.add(src)
#     tar.close()
#
#     md5zidian = {}
#     for path,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5zidian[key] = check_md5(key)
#
#     with open( md5,'wb') as fobj:
#         pickle.dump(md5zidian,fobj)
#
# def incrback(src,dst,md5):
#
#     fname = os.path.basename(src)
#     fname = '%s_incr_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
#     fname = os.path.join(dst,fname)
#     print(fname)
#
#     with open(md5,'rb') as fobj:
#         old_md5=pickle.load(fobj)
#
#     md5zidian = {}
#     for path, folders, files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5zidian[key] = check_md5(key)
#
#     with open(md5,'wb') as fobj:
#         pickle.dump(md5zidian,fobj)
#
#     tar = tarfile.open(fname,'w:gz')
#     for key in md5zidian:
#         if md5zidian[key] != old_md5.get(key):
#             tar.add(key)
#     tar.close()
#
# if __name__ == '__main__':
#     src = '/pythondata/security'
#     dst = '/pythondata'
#     md5 = '/pythondata/md5.data'
#
#     if time.strftime('%a') == 'Mon':
#         fullback(src,dst,md5)
#     else:
#         incrback(src,dst,md5)


















