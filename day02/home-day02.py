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
######14-成绩分类1
cj = int(input('请输入成绩:'))
if cj > 90:
    print('优秀')
elif cj > 80:
    print('好')
elif cj > 70:
    print('良')
elif cj > 60:
    print('及格')
else:
    print('冒搞手')
