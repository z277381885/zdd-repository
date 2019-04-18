# # username = input('username:')
# # print('welcome', username)
# # print('welcome' + username)
#
# # import this
#
# a = 10 < 15 < 20
# print(a)
# namber_a = 3
# namber_b = 10 + 5
# namber_c = namber_a + 1
# print(namber_a, namber_b, namber_c)
#
# namber_d = 5 / 3
# namber_e = 5 // 3   #商
# namber_f = 5 % 3    #取余
# namber_g = divmod(5,3) #同时得到商和余数
# namber_h = 2 ** 3
# namber_i = 10 < 15 <20
# namber_j = 10<20 and 20>15
# print("d:",namber_d,"    ",
#       "e:",namber_e,
#       "f:",namber_f,
#       "g:",namber_g,
#
#       "h:",namber_h,"i:",namber_i,"j:",namber_j)
# #
# test_1 = 11
# test_2 = 0o11   #8进制
# test_3 = 0x11   #16进制
# test_4 = 0b11   #2进制
# print(test_1,test_2,test_3,test_4)
#
# #字符串输出
# print('tom\'s pet is cat')
# print("tom's pet is cat")
#
# print("I am %s" % 'zdd')   #将参数zdd传送给%s
# print("%s is %s years old" % ('zdd',20))
#
# #三引号,保留格式,,是三个单引号或者三个双引号
# test_5='''hello
# hi
# gret'''
# print(test_5)
#
# py_str = 'python'
# print(len(py_str))
# print(py_str[0])        #取出第1个字符
# print(py_str[1])        #取出第2个字符
# print(py_str[2])
# print(py_str[3])
# print(py_str[4])
# print(py_str[5])        #取出第6个字符
# print(py_str[-1])       #取出倒数第1个字符
# print(py_str[-2])       #取出倒数第2个字符
# print(py_str[2:4])      #取出第三个到第5个字符
# print(py_str[2:])       #结尾不写,从第三个到结尾
# print(py_str[:2])      #开头不写,从第一个开始取,取第三个的前面的所有
# print(py_str[::2])      #设置步长,隔两个取一个
# print(py_str[0::2])     #设置步长为2,从第一个开始取
#
# # 拼接和重复
#
# # 列表
# print("----列表----")
# alist = [10, 20, 30, 'tom','jerry' ]
# print(alist)
# print(len(alist))   #统计个数
# print(alist[0])
# print(alist[1])
# print(alist[3:])
# print(10 in alist)  #判断10是否在列表alist中
# alist[0] = 1000     #列表
# print(alist)
# alist.append('zdd')
# print(alist)

# print("----元组:可认为是静态的列表---")
# atuple = (100,20,30,'tom','jerry','bob')
# print(atuple)
# print(atuple[0])
# print(atuple[:3])
# print(20 in atuple)     #判断
#
# # atuple[0] = 10    #不支持修改
# # print(atuple)
#
# print("---字典--")
# adict = {'name':'bob','age':22}
# print(adict)
#
# print('--表达式--')
# if 3 > 0:
#     print('yes')
#     print('*' * 10)
#
# if 'th' in 'python':
#     print('th in python, yes')
#     print('*' * 20)
#
# if -0.0:        #任何值为0的数字都是false,-0也是false
#     print('yes')
#
# if 250:
#     print('非0数字都是ture')
#     print('*' * 40)
#
# if '   ':
#     print('#任何非空字符都是true,空格也是一个字符')
#     print('*' * 40)
# if '':          #空字符串为false
#     print('yes')
#
# if [False]:     #不仅仅是列表,任何非空元组,非空字典都是true
#     print('这是一个非空列表,true')
#     print("*" * 40)
#
# if  []:         #空列表为false
#     print('yes')
#
# if (100,20):    #非空元组
#     print('非空元组:yes')
#     print('*' * 40)
# if {'name':'zdd'}:
#     print('非空字典:yes')
#
# print('*' * 40)

# import getpass
# username = input("username:")
# password = getpass.getpass("password:")
# if username == 'zdd':
#     if password == '123456':
#         print('yes')
#     else:
#         print('no')
# else:
#     print('no')

###########################################
# import getpass
# username = input('username:')
# password = getpass.getpass('password:')
# if username == 'zdd' and password == '123456':
#     print('登录成功')
# else:
#     print('登录失败')
########################################
#猜数字游戏
# import random               #调用random 函数,
# num = random.randint(1,5)   #随机数在1-5之间
# answer = int(input('guess the number:'))   #输入数字类型为int
# print('随机数是:',num)
# if answer > num:
#     print('猜大了')
# elif answer < num:
#     print('猜小了')
# else:
#     print('猜对了')
######################################
#判断成绩
# cj = int(input('请输入成绩:'))
# if cj > 100:
#     print('输入错误,请重新输入')
# elif cj >= 90:
#     print('优秀')
# elif cj >= 80:
#     print('好')
# elif cj >= 70:
#     print('还行')
# elif cj >= 60:
#     print('极度危险')
# else:
#     print('垃圾')
################################
#判断成绩方法二
# score = int(input('分数:'))     #将用户输入的字符转换成数字
# if 0 <= score < 60:
#     print('垃圾')
# if 60 <= score < 70:
#     print('极度危险')
# if 70 <= score <80:
#     print('还行')
# if 80 <= score <90:
#     print('好')
# if 90 <= score <=100:
#     print('优秀')
# if 100 < score:
#     print('请重新输入')
#################################################
#小技巧
# a = 10
# b = 10
# if a < b:
#     s = a
# else:
#     s = b
# print('s:',s)
# #以上四行可以精简为以下一行
# a = 10
# b = 20
# small = a if a < b else b
# print('small:',small)
###################################################
#猜数字游戏--自己写
# import random               #调用random 函数,
# a = random.choice(['石头','剪刀','布'])
# b = input('游戏开始,请出猪蹄:')
# print(a)
# if a == '石头':
#     if b == a:
#         print('平局')
#     elif b == '剪刀':
#         print('你输了')
#     else:
#         print('你赢了')
# elif a == '剪刀':
#     if b == a:
#         print('平局')
#     elif b == '石头':
#         print('赢了')
#     else:
#         print('你输了')
# else:
#     if b == a:
#         print('平局')
#     elif b == '石头':
#         print('你输了')
#     else:
#         print('你赢了')
#猜数字游戏---自己写代码2
# import random               #调用random 函数,
# a = random.choice(['石头','剪刀','布'])
# b = input('游戏开始,请出猪蹄:')
# print('你输入的是:%s,   计算机出的是:%s' % (b,a))
# if a=='石头' and b=='布' or a=='剪刀' and b=='石头' or a=='布' and b=='剪刀':
#     print( '赢了')
# elif a == b:
#     print('平局')
# else:
#     print('输了')
##猜数字游戏---小列表方式
# import random
# all_a = ['石头','剪刀','布']
# all_win = [['石头','剪刀'],['剪刀','布'],['布','石头']]   #小列表
# computer = random.choice(all_a)
# player = input('请亮出你的猪蹄样式(石头/剪刀/布):')
# print('你亮出的猪蹄样式是:%s,    计算机出的是:%s' % (player, computer))
# if player == computer:
#     print('所以是:\033[32;1m平局\033[0m')
# elif [player, computer] in all_win:
#     print('所以你:\033[31;1m赢了\033[0m')
# else:
#     print('所以你:\033[33;1m输了\033[0m')
###猜拳游戏---利用保持格式输出和下标
# import random
# all_a = ['石头','剪刀','布']
# all_win = [['石头','剪刀'],['剪刀','布'],['布','石头']]   #小列表
# computer = random.choice(all_a) #电脑随机产生的字符
# prompt = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请选择(0/1/2):'''          #保持格式输出,分四行输出
# ind = int(input(prompt))    #将用数输入的字符(0或者1或者2)转换成数字
# player = all_a[ind]         #利用ind产生的数字,到all_a;列表里面找字符
# print('你亮出的猪蹄样式是:%s,  计算机出的是:%s' % (player, computer))   #显示人机选择结果
# if player == computer:                      #
#     print('所以是:\033[32;1m平局\033[0m')
# elif [player, computer] in all_win:
#     print('所以你:\033[31;1m赢了\033[0m')
# else:
#     print('所以你:\033[33;1m输了\033[0m')
########################################################
####while 循环
# result = 0
# counter = 1
# while counter <= 100:
#     result += counter
#     counter += 1
# print(result)
##while 循环应用猜随机数--break终止整个循环############
# import random
# num = random.randint(1, 100)        #调用1-100之间的随机数
# while 1:
#     a = int(input('猜一个数字:'))
#     if a > num:
#         print('猜大了')
#     elif a < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break                             #终止循环
##while 循环应用,数字累加,continue终止本次循环
##完善石头剪刀布小游戏:实现
# import random
# all_jq = ['石头','剪刀','布']                            #定义出拳的所有结果
# all_win = (['石头','剪刀'],['剪刀','布'],['布','石头'])   #定义赢的所有可能
# promptaa = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请输入(0/1/2):'''                    #promtaa随便取名,三引号保持格式输出
# cs_zs = 0                           #定义总共出的次数
# cs_win = 0                          #定义总共赢的次数
# while cs_win < 3:                   #如果总共赢得总次数少于3,则继续循环
#     jc = random.choice(all_jq)      #random.choice在元素组里面随机抽取字符
#     rc_1 = int(input(promptaa))     #int将输入的字符转为数字
#     rc_2 = all_jq[rc_1]             #rc_1为all_jq的下标
#     print('你出的是:%s,  计算机出的是:%s' % (rc_2, jc))  #%s %s % (变量1,变量2) 格式为传参
#     cs_zs += 1          #总的次数加1
#     if [rc_2,jc] in all_win:
#         print('这局你:\033[31;1m赢了\033[0m')
#         cs_win += 1     #赢的次数加1
#     elif rc_2 == jc:
#         print('这局是:\033[32;1m平局\033[0m')
#     else:
#         print('这局你:\033[33;1m输了\033[0m')
# print('总共猜了:%s局 猜赢了:%s局' % (cs_zs,cs_win))
########################################################################
#完善石头剪刀布小游戏:实现三局两胜
# import random
# all_jq = ['石头','剪刀','布']                            #定义出拳的所有结果
# all_win = (['石头','剪刀'],['剪刀','布'],['布','石头'])   #定义赢的所有可能
# promptaa = '''(0) 石头
# (1) 剪刀
# (2) 布
# 请输入(0/1/2):'''                    #promtaa随便取名,三引号保持格式输出
# cs_zs = 0                           #定义总共出的次数
# cs_win = 0                          #定义总共赢的次数
# cs_jy = 0
# while cs_win < 2 and cs_jy < 2:      #如果总共赢得总次数少于3,则继续循环
#     jc = random.choice(all_jq)      #random.choice在元素组里面随机抽取字符
#     rc_1 = int(input(promptaa))     #int将输入的字符转为数字
#     rc_2 = all_jq[rc_1]             #rc_1为all_jq的下标
#     print('你出的是:%s,  计算机出的是:%s' % (rc_2, jc))  #%s %s % (变量1,变量2) 格式为传参
#     cs_zs += 1          #总的次数加1
#     if [rc_2,jc] in all_win:
#         print('这局你:\033[31;1m赢了\033[0m')
#         cs_win += 1     #赢的次数加1
#     elif rc_2 == jc:
#         print('这局是:\033[32;1m平局\033[0m')
#     else:
#         print('这局你:\033[33;1m输了\033[0m')
#         cs_jy += 1
# if cs_win > cs_jy:
#     print('人类先赢%s,总共猜了:%s局,机器猜赢了:%s' % (cs_win,cs_zs,cs_jy))
# else:
#     print('机器先赢%s,总共猜了:%s局,人类猜赢了:%s' % (cs_jy,cs_zs,cs_win ))
####

###else语句############################
###在python中,循环也有else语句,else语句,只在循环完成后执行,break语句也会跳过else语句
###猜数字游戏.猜的次数不能超过三次,
### 如果三次没猜对则告诉你正确答案. 执行print('游戏结束,正确的结果是: %s' % num)
### 如果三次内猜对了,则不输出正确答案
# import random
# num = random.randint(1,10)
# counter = 0
#
# while counter < 3:
#     counter += 1
#     answer = int(input('请输入数字:'))
#     if answer > num:
#         print('猜大了')
#     elif answer < num:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
# else:                   #如果执行了break,则不再执行else,否则会执行下面
#     print('游戏结束,正确的结果是: %s' % num)

###for循环#遍历##############################################################
# chs = 'hello'
# alist = ['bob','zdd','alice']
# atuple = (10,20)
# adict = {'name': 'tom', 'age': '23', 'like':'ball'}
#
# for ch in chs:            #ch随便命名,
#     print(ch)
#
# for name in alist:
#     print(name)
#
# for i in atuple:
#     print(i)
#
# for key in adict:
#     print('%s: %s' % (key, adict[key]) )
###range函数############################################################
###for循环常与range函数一起使用,range函数提供循环条件
###range函数的完整语法为: range(start,end,step =1)  range(开始值,结束值,步长)
# print(range(10))            #range(0, 10) 不生成列表,节省空间,可直接使用
# for i in range(10):
#     print(i)                #按1-9输出9行,10不包含,10为结束值不包含
# print(list(range(10)))      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     #生成列表
# print(list(range(6,10)))    #[6, 7, 8, 9]  注意:10不包含,不包含结束值
# print(list(range(1,10,2)))  #[1, 3, 5, 7, 9]  1开始,步长值为2,
# print(list(range(10,0,-1))) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list(range(10,0,-2))) #[10, 8, 6, 4, 2]
# print(list(range(10,0,2))) #[]      #步长必须为-2
####斐波那契数列,计算10个数字的斐波拉契数列###
# number = int(input('请输入要计算的斐波那契数列范围:'))
# alist = [0,1]                   #定义最初始的列表,占用两个了
# for i in range(number-2):       #如果输入了10 ,实际运行要减去2个,实际是8,
#     alist.append(alist[-1] + alist[-2])   #将列表中最后一个数加上倒数第二个的和,添加到列表中
# print(alist)                #输入20 得到结果[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
####九九乘法表,输入乘法表的范围#####
# number_99 = int(input('请输入乘法表的范围'))
# for i in range(1,number_99):        #range默认是从0开始,所以定义一个开始值1
#     for j in range(1,i+1):
#         print('[%s*%s=%s] '  % (i,j,i*j),end='')
#     print( )             #print()默认输出一个回车
###列表解析##########
# print([10])
# print([10 + 5])
# print([10 + 5 for i in range(8)])
# print([10 + 5 for i in range(0,8)])     #与上一行一样
# print([10 + 5 for i in range(1,8)])     #比上一行少一个
# print([10 + i for i in range(5)])       #
# print([10 + i for i in range(1,5)])     #[11, 12, 13, 14]
# print([10 + i for i in range(1,6) if i % 2 == 1]) #[11, 13, 15]  #满足判断条件才保留
###ip地址##########
# print(['192.168.1.%s' % 1])
# print(['192.168.1.%s' % i  for i in range(1,10)])
#
#
#####文件#######################################################
###1.read,默认读取文件的全部内容
# f = open('/tmp/passwd1')    #打开文件
# data =
#              #读取文件
# print(data)                 #输出
# #读取文件时,文件指针会向后移动,读取全部内容后文件指针已经到结尾,再读就没有内容了
# # data = f.read()
# # print(data)
# data2 = f.read()
# print(data2)         #data2是没有数据的,因为第一个data = f.read()全部读取完毕了
# data = f.close()     #关闭
#
# f = open('/tmp/passwd2')
# data = f.read()        #取前面四个字符
# print(data)
# data2 = f.read(4)       #接着上面再读取四个字符
# print(data2)
# f.close()               #关闭f 打开的文件
# print(f.read(4))     #报错,已经被关闭ValueError: I/O operation on closed file.

###2.readline,读一行####
# f = open('/tmp/passwd1')
# a = f.readline()            #读取第一行
# print(a)
# b = f.readline()            #接着上面读取第二行
# print(b)

# f = open('/tmp/passwd1').readline()     #不建议使用,无法读取第二行
# print(f)

##3.readlines  读取所有行,放到列表中,
# f = open('/tmp/passwd2')
# a = f.readlines()
# print(f)           #输出一个列表,每个value就是文件中的一行


###4.通过for循环进行遍历,常用,需要记住
# f = open('/tmp/passwd2')
# for line in f:
#     print(line,end='')
# f.close()                   #关闭

###5.读取非文本文件
# f = open('/tmp/windows.jpg')
# a = f.read(4)   #报错,默认情况下,文件被认为是文本文件,python试图将取出的4字节转换成文字,图片无法转换成文字
# f.close()

# f = open('/tmp/windows.jpg','rb')   #以rb的方式打开,
# print(f.read(4))       #输出b'\xff\xd8\xff\xe0'  16进制数,python将2进制以16进制方式进行显示
# print(f.read(4))        #输出b'\x00\x10JF'        #接着上面的显示
# f.close()

# f = open('/tmp/windows.jpg','rb')   #以rb的方式打开,
# print(f.read(8))                    #输出b'\xff\xd8\xff\xe0\x00\x10JF'
# f.close()
#### 注意:1,read读取一般可以读取4096字节,正好为1个block大小
####     2,文本文件也可以以rb方式打开
###r,以读方式打开(文件不存在则报错)
###w,以写方式打开(文件存在则清空,不存在则创建)
###a,以追加模式打开,(必要时创建新文件)
###b,以二进制模式打开,以bytes方式打开(直接显示为2进制的方式)
###r+/w+/a+,以读写模式打开

###6,写入####
# f = open('/tmp/passwd1','w')
# a = f.write('hello world!\n')       #没有则创建.有的话就清空再写入,
# b = f.write('hello world!\n')
# # c = f.writelines('hello world!\n')  #???????????
# print(a,b,)
#[root@room9pc01 tmp]# cat passwd1         查看实际文件内容
#hello world!
#hello world!.

# f = open('/tmp/passwd1','w')
# a = f.writelines(['2nd line.', '3rd line.\n'])
# print(a)
# f.close()   #关闭,也写入数据
###[root@room9pc01 tmp]# cat passwd1        #查看实际文件内容
###2nd line.3rd line.

###7.with子句:语句结束,文件自动关闭
# with open('/tmp/passwd1') as f:
#    print( f.readline() )            #显示文件的内容:2nd line.3rd line.
#
# # print(f.readline())             #继续执行.报错,file已closed

###8.文件指针#######以后用不着
# f = open('/tmp/passwd','rb')
# print(f.tell())                 #输出0,
# f.read(5)                       #读取5个字节后
# print(f.tell())                 #查看输出5,指针偏移5个字节
#####
###seek函数用与移动文件指针,有两个参数.第二个参数表示相对位置.
###第二个参数(0表示开头,1表示当前位置.2表示结尾),第一个参数是相对于第二个参数的偏移量
# f = open('/tmp/passwd1','rb')
# print(f.tell())         #当前指针位置0
# print(f.read(5))        #输出b'2nd l'         #文件原文2nd line.3rd line.
# print(f.seek(3,1))      #输出8,,1表示当前位置.3表示偏移5个字节
# print(f.readline())     #输出b'.3rd line.\n'   #文件原文2nd line.3rd line.
...


###编写一个copy命令..将一个文件拷贝到
# src_fname = '/bin/ls'           #定义源文件
# dst_fname = '/tmp/ls'           #定义目标文件
#
# src_fobj = open(src_fname,'rb')     #打开源文件,以rb方式
# dst_fobj = open(dst_fname, 'wb')
#
# while 'true':                   #无限制读取
#     data = src_fobj.read(4096)  #因为读取数据是放入内存,所以每次读取只读取4字节
#     # if data == b'':           #判断方式1,data数据等于空,则表示数据取完,执行break
#     # if len(data) == 0:        #判断方式2,统计data变量的数据长度,等于0,表示数据取完,执行break
#     if not data:                #判断方式3,如果data变量是空字符串,则False.
#         break                   #终止所有循环
#     dst_fobj.write(data)        #将data变量值写入dst_fobj,参考上面写入练习
#
# src_fobj.close()
# dst_fobj.close()
###验证,电脑上操作如下############
###[root@room9pc01 tmp]# md5sum ls
###918cb545b3458e1bf18b712b36af304f  ls
###[root@room9pc01 tmp]# md5sum /bin/ls
###918cb545b3458e1bf18b712b36af304f  /bin/ls

#####函数#######################
#####定义一个斐波拉契函数
# def gen_fib():
#     number = int(input('请输入要计算的斐波那契数列范围:'))
#     alist = [0,1]                    #定义最初始的列表,占用两个了
#     for i in range(number-2):        #输入了10 ,实际运行要减去2个,
#         alist.append(alist[-1] + alist[-2])   #将列表中最后一个数加上倒数第二个的和,添加到列表中
#     # print(alist)    #输入5 得到结果[0, 1, 1, 2, 3] 函数中不用这个输出,否者固定在函数中输出
#     return alist      #将最后得到的alist 列表结果返回给函数gen_fib(),函数结果需要return返回
#                       #如果没有return返回,默认函数返回值为none
# mylist = gen_fib()       #调用函数执行,并且将函数值定义给变量mylist
# print(mylist)            #输出mylist变量值
# ####
#####定义一个斐波拉契函数,使用函数参数,不是input输入的参数
# def gen_fib(n):
#  ####number = int(input('请输入要计算的斐波那契数列范围:'))在这不再手动输入,在函数gen_fib(n)中调用n参数
#     alist = [0,1]                    #定义最初始的列表,占用两个了
#     for i in range(n-2):        #这里接受参数n.输入了10 ,实际运行要减去2个,
#         alist.append(alist[-1] + alist[-2])   #将列表中最后一个数加上倒数第二个的和,添加到列表中
#     # print(alist)    #输入5 得到结果[0, 1, 1, 2, 3] 函数中不用这个输出,否者固定在函数中输出
#     return alist      #将最后得到的alist 列表结果返回给函数gen_fib(),函数结果需要return返回
#
# mylist = gen_fib(10)   #调用函数执行,定义参数"5"(5可随意改变),执行,并且将函数结果定义给变量mylist,
# print(mylist)            #输出mylist变量值
# new_list = [10 + i for i in mylist]         #新列表,mylist列表中的每个值+10
# print(new_list)
# mylist = gen_fib(20)
# print(mylist)
####函数默认值##
# def gen_fib(n=10):          #定义默认参数n=10
#     #number = int(input('请输入要计算的斐波那契数列范围:'))在这不再手动输入,在函数gen_fib(n)中调用n参数
#     alist = [0,1]                    #定义最初始的列表,占用两个了
#     for i in range(n-2):        #这里接受参数n.输入了10 ,实际运行要减去2个,
#         alist.append(alist[-1] + alist[-2])   #将列表中最后一个数加上倒数第二个的和,添加到列表中
#     # print(alist)    #输入5 得到结果[0, 1, 1, 2, 3] 函数中不用这个输出,否者固定在函数中输出
#     return alist      #将最后得到的alist 列表结果返回给函数gen_fib(),函数结果需要return返回
#
# mylist = gen_fib()   #调用函数执行,未传参,将会以默认参数n=10执行
# print(mylist)
###函数的位置参数###
# import sys
#
# print(sys.argv)     #argv是sys位置函数模块的参数列表,将位置参数存到该列表中
###[root@room9pc01 day02]# python3 day02.py
###['day02.py']
###[root@room9pc01 day02]# python3 day02.py 123 456
###['day02.py', '123', '456']

###将cp命令套上位置参数--不是函数方式
# import sys                        #调用位置参数
# src_fname = sys.argv[1]           #定义源文件
# dst_fname = sys.argv[2]           #定义目标文件
#
# src_fobj = open(src_fname,'rb')     #打开源文件,以rb方式
# dst_fobj = open(dst_fname, 'wb')
#
# while 'true':                   #无限制读取
#     data = src_fobj.read(4096)  #因为读取数据是放入内存,所以每次读取只读取4字节
#     # if data == b'':           #判断方式1,data数据等于空,则表示数据取完,执行break
#     # if len(data) == 0:        #判断方式2,统计data变量的数据长度,等于0,表示数据取完,执行break
#     if not data:                #判断方式3,如果data变量是空字符串,则False.
#         break                   #终止所有循环
#     dst_fobj.write(data)        #将data变量值写入dst_fobj,参考上面写入练习
#
# src_fobj.close()
# dst_fobj.close()

# ###执行结果,以及md5sum验证文件
# ###[root@room9pc01 day02]# ls
# ###day02.py  day03.py  home-day02.py
# ###[root@room9pc01 day02]#
# ###[root@room9pc01 day02]#
# ###[root@room9pc01 day02]# python3 day02.py home-day02.py test.py
# ###[root@room9pc01 day02]# ls
# ###day02.py  day03.py  home-day02.py  test.py
# ###[root@room9pc01 day02]# md5sum home-day02.py
# ###bcd17d976578c12c74e537f7e64e8375  home-day02.py
# ###[root@room9pc01 day02]# md5sum test.py
# ###bcd17d976578c12c74e537f7e64e8375  test.py

###copy程序.函数形式
# import sys
# def copy(src_fname, dst_fname):         #定义函数,并定义两个参数
#     src_fobj = open(src_fname,'rb')     #打开源文件,以rb方式
#     dst_fobj = open(dst_fname, 'wb')
#
#     while 'true':                   #无限制读取
#         data = src_fobj.read(4096)  #因为读取数据是放入内存,所以每次读取只读取4字节
#         # if data == b'':           #判断方式1,data数据等于空,则表示数据取完,执行break
#         # if len(data) == 0:        #判断方式2,统计data变量的数据长度,等于0,表示数据取完,执行break
#         if not data:                #判断方式3,如果data变量是空字符串,则False.
#             break                   #终止所有循环
#         dst_fobj.write(data)        #将data变量值写入dst_fobj,参考上面写入练习
#
#     src_fobj.close()
#     dst_fobj.close()
# copy(sys.argv[1],sys.argv[2])       #调用参数
##执行以及验证结果
###[root@room9pc01 day02]# ls
###day02.py  day03.py  home-day02.py  test.py
###[root@room9pc01 day02]# python3 day02.py home-day02.py test2.py
###[root@room9pc01 day02]# ls
###day02.py  day03.py  home-day02.py  test2.py  test.py
###[root@room9pc01 day02]# md5sum home-day02.py test2.py
###bcd17d976578c12c74e537f7e64e8375  home-day02.py
###bcd17d976578c12c74e537f7e64e8375  test2.py

##所有字母大小写+所有数字##########
# import string  # 导入string这个模块
# print(string.digits)  # 输出包含数字0~9的字符串
# print(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
# print(string.ascii_lowercase)  # 包含所有小写字母的字符串
# print(string.ascii_uppercase)  # 包含所有大写字母的字符串
# print(string.punctuation)      # 所有特殊字符

##随机密码,用户自己定义密码长度
# import string,random
# all_dx = string.ascii_letters
# all_sx = string.digits
# all = all_dx + all_sx
# allist = []
# def suiji(n=8):
#     for i in range(n):
#         sj_1 = random.choice(all)
#         allist.append(sj_1)
#     return allist
# mm_cd = int(input('请输入密码长度: '))
# mm = suiji(mm_cd)
# print(mm)
##随机密码,用户自己定义密码长度
# import string,random
# all_dx = string.ascii_letters
# all_sx = string.digits
# all = all_dx + all_sx
# def suiji(n=8):
#     mm = ''
#     for i in range(n):
#         sj_1 = random.choice(all)
#         mm  += sj_1
#     return mm
# mm_cd = int(input('请输入密码长度: '))
# a = suiji(mm_cd)
# print(a)
##################day-04#############################day-04###
######模块
####1文件:是python从物理上组织代码的形式,
####2模块:是python从逻辑上组织代码的形式,
# hi = 'hello zdd'
# def pstar(n=30):
#     print('$' * n)
###实际执行如下#########
# ###[root@room9pc01 tmp]# cd /root/PycharmProjects/day02/
# ###[root@room9pc01 day02]# python3
# ###>>> import day02                   #python文件全名为:day02.py
# ###>>> day02.hi
# ###'heelo zdd'
# ###>>> day02.pstar(
# ###... )
# ###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ###>>> day02.pstar()
# ###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ###>>>
#####创建模块
###导入模块
#使用import导入就会执行一遍语句
# hi = 'heelo zdd'
# def pstar(n=30):
#     print('$' * n)
# pstar()
# pstar(40)
# [root@room9pc01 day02]# python3 day02.py   #直接执行
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# [root@room9pc01 day02]# python3
# Python 3.6.1 (default, Apr 27 2018, 04:53:30)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import day02                #调用这个模块也会执行一遍
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# >>>

###模块导入的特性"_name_",     #利用这个特性可空值模块的执行方式
###当模块文件直接运行时,_name_的值是:'_main_'
###当模块文件被导入时,_name_的值是:该模块的名字
# hi = 'heelo zdd'
# def pstar(n=30):
#     print('$' * n)
# if __name__ == '__main__':  #如果是直接运行python就执行下面
#     pstar()
#     pstar(40)
###[root@room9pc01 day02]# python3 day02.py
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#################################################
# hi = 'heelo zdd'
# def pstar(n=30):
#     print('$' * n)
# if __name__ == 'day02':
#     pstar()
#     pstar(40)
# ##[root@room9pc01 day02]# python3
# ##>>> import day02                 #如果是import调用才执行
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#####随机密码###########
# from random import choice
# from string import ascii_letters,digits    #/usr/local/lib/python3.6/string.py
#
# all_chs = ascii_letters + digits
# def gen_pass(n=8):
#     result = ''
#     for i in range(n):
#         ch = choice(all_chs)
#         result += ch
#     return (result)
# if __name__ == '__main__':
#     print(gen_pass())
#     print(gen_pass(4))


#####shell相关模块###############
###shutil:shell工具
###1,shutil.copyfileobj()
# import shutil
# file_a = open('/etc/issue','rb')
# file_b = open('/tmp/issue1','wb')
# shutil.copyfileobj(file_a,file_b)
# file_a.close()
# file_b.close()
# ####实际结果
# [root@room9pc01 tmp]# cat /etc/issue
# \S
# Kernel \r on an \m
#
# [root@room9pc01 tmp]# cat /tmp/issue1
# \S
# Kernel \r on an \m
#
# ###2,shutil.copy 拷贝文件,  #常用
# import shutil
# shutil.copy('/etc/issue.net','/tmp')
#
# [root@room9pc01 tmp]# ls /tmp/issue*
# /tmp/issue1  /tmp/issue2
#
# ###3,shutil.copy2()       #相当于cp -p
# ###4,shutil.move()        #mv文件     #常用
# import shutil
# shutil.move('/tmp/issue.net','/hahahahah')
#
# ###5,shutil.remtree()   #rm -rf  但是只能删除目录,不能删除文件.常用
# import shutil


######变量复制,多重赋值#################
# x = y = 10
# print(x)
# print(y)
#
# a , b = 10 ,20
# print(a , b)
# aa , bb = (10,20)
# print(aa,bb)
# aaa,bbb = [10,20]
# print(aaa,bbb)
# a, b = b, a  # 互换a和b的值
# print( a,b)
######合法标识符########################
#######关键字#########################
# import keyword          #关键字列表和iskeyword函数模块
# print(keyword.kwlist)
# print(keyword.iskeyword('pass'))                  #输出:True,说明pass是关键字
# print(keyword.iskeyword('adp'))                   #输出:False,说明adp不是关键字
######内建########################
##内建不要被覆盖

###模块布局###########
# ! /usr/bin/env python
# "this is a test module"
# import sys,os
#
# def get_fname():
#     while True:
#         fname = input('请输入文件名: ')
#         if not os.path.exists(fname):       #判断文件名是否已存在,如果存在则执行
#             break
#         print('该文件已存在,请重试!')
#     return fname
#
# def get_content():
#     content = []
#     print('请输入内容,另起一行输入"end"结束!')
#     while True:
#         line = input('> ')
#         if line == 'end':           #判断输入的是否是结束
#             break
#         content.append(line)        #将line的内容添加到content列表中
#     return content
#
# def wfile(fname, content):
#     with open(fname,'w') as fobj:
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     fname = get_fname()         #fname得到get_fname():中产生的不存在同名的文件名
#     content = get_content()     #content得到get_content():中的产生的列表内容
#     content = [line + '\n' for line in content] #将content列表所有value添加一个\n
#     wfile(fname,content)        #将content的内容写入到名为fname的文件中,没有则创建

##########
# alist = ['tom','bob','jerry','alice']
#
# for i_1 in [0,1,2,3]:
#     print('%s : %s' % (i_1,alist[i_1]))
#
# for i_2 in range(4):
#     print('%s : %s' % (i_2, alist[i_2]))
#
# for i_3 in range(len(alist)):
#     print('%s : %s' % (i_3, alist[i_3]))
#
# print(list(enumerate(alist)))   #[(0, 'tom'), (1, 'bob'), (2, 'jerry'), (3, 'alice')]
#
# for i_4 in enumerate(alist):
#     print('%s :　%s' % (i_4))        #必需两个%s
#
# for i_5, i_6 in enumerate(alist):
#     print('%s:%s' % (i_5,i_6))      #与上一样，这种分两个变量更灵活，
# #以上所有输出都一样如下
# # 0:tom
# # 1:bob
# # 2:jerry
# # 3:alice
# ###
# alist = ['tom','bob','jerry','alice']
# print(reversed(alist))          #输出一个文件:<list_reverseiterator object at 0x7f2e1c9274e0>
# print(list(reversed(alist)))    #翻转，但是列表本身不变,输出['alice', 'jerry', 'bob', 'tom']
# print(alist.reverse())          #翻转，改变列表本身
#
# print(sorted(alist))            #排序，但是列表本身不变，输出['alice', 'bob', 'jerry', 'tom']
# print(list(sorted(alist)        #排序，但是列表本身不变，输出['alice', 'bob', 'jerry', 'tom']
# print(alist.sort())             #排序，改变列表本身


#####
# import sys
# import keyword,string
#
# first_chs = string.ascii_letters + '_'
# other_chs = first_chs + string.digits
#
# def check_idt(idt):
#     if keyword.iskeyword(idt):
#         return '% 是关键字' % idt
#
#     if not idt[0] in first_chs:
#         return '第一个字符不合法'
#
#     for ind,ch in enumerate(idt[1:]):
#         if ch not in other_chs:
#             return '第%s 个字符不合法' % (ind + 2)
#
#     return '%s 是合法的标识符' % idt
#
# if __name__ == '__main__':
#     print(check_idt(sys.argv[1]))

####执行之后的结果##############
# [root@room9pc01 day02]# python3 day02.py  asdf
# asdf 是合法的标识符
# [root@room9pc01 day02]# python3 day02.py  123sdfa
# 第一个字符不合法
# [root@room9pc01 day02]# python3 day02.py  asdf@sdf
# 第5 个字符不合法

####字符串格式化 ###########
###1,基础样式
# print('%s' % 'bob')

# print('%s is %s years old' % ('bob',20))  #bob is 20 years old
# print('%s is %d years old' % ('bob',20))   #s用d代替,为有符号的十进制:bob is 20 years old

# print('%10s%8s' % ('name','age'))   #name点10个宽度,age占8个宽度
# print('%10s%8s' % ('zdd',20))
# print('%-10s%-8s' % ('zdd',20))     #加-号
#
###了解
# print('%#o' % 10)   #8进制
# print('%#x' % 10)   #16进制
# print('%f' % (5 / 3))   #f为浮点数
# print('%5.2f' % (5 / 3))
# print('%+d' % 10)       #正数前加+号
# print('%+d' % -10)      #负数不需要加,就是-号
#
# ###format函数####位置参数###########
# print('{} is {} years old'.format('bob',20))    #bob is 20 years old
# print('{0} is {1} years old'.format(20,'bob'))  #20 is bob years old
# print('{1} is {0} years old'.format(20,'bob'))  #bob is 20 years old
# print( '{1:<10}:{0:>8}'.format(20, 'bob'))      #位置1的bob左对齐点10个宽度)
# ###创建用户##########
# import sys
# import subprocess
# from randpass2 import gen_pass
#
# def adduser(user, passwd, fname):
#     info = '''用户信息
# 用户名:%s
# 密码:%s
#
# ''' % (user,passwd)
#
#     subprocess.run('useradd %s' % user, shell=True)
#     subprocess.run(
#         'echo %s | passwd --stdin %s' % (passwd,user),
#         shell=True
#     )

#     with open(fname,'a') as fobj:
#         fobj.write(info)
#
# if __name__ == '__main__':
#     username = sys.argv[1]
#     pwd = gen_pass()
#     filename = '/tmp/users.txt'
#     adduser(username,pwd,filename)

#######原始字符串#########################################
# win_path = 'c:\temp'
# print(win_path)             #输出c:	emp
#
# win_path = 'c:\\temp'
# print(win_path)             #输出c:\temp
#
# wpath = r'c:\temp'          #原始字符串,字符串中的字符是本身含义  #字符串使用次数特别多
# print(wpath)                #输出c:\temp
###字符串常用办法#####
###1、去除空白字符
# s1 ='  hello world\n'
# print(s1)
# print(s1.strip())           #去除两边的空白字符，包括换行
# print(s1.lstrip())          # 去除左边空白字符
# print(s1.rstrip())          #去除右边空白字符，包括换行
###2、切割字符###
# s2 = 'hello world ni hao'
# print(s2)
# print(s2.split())
# s3 = 'hello-world-ni-hao'
# print(s3.split())
# print(s3.split('-'))
###3、拼接字符####
# slist = ['hello','world','in','hao']
# print(slist)
# print(''.join(slist))
# print(' '.join(slist))
# print('--'.join(slist))
###4、对齐###
# s2 = 'hello world ni hao'
# print(s2.center(50))
# print(s2.center(50),'-')
# print(s2.center(50,'-'))
# print(s2.rjust(50,'-'))
# print(s2.ljust(50,'-'))
# ###5判断开头结尾
# s2 = 'hello world ni hao'
# print(s2.startswith('h'))
# print(s2.startswith('he'))
# print(s2.startswith('hea'))
# print(s2.endswith('o'))
# print(s2.endswith('ao'))
# print(s2.endswith('sao'))
####格式化输出#####自己写的
# a = ['nihao','zdd']
# width = 48
# # contents = get_contents()
# print('+%s+' % ('*' * 48))
# for line in a:
#     print('+{:^48}+'.format(line))
# print('+%s+' % ('*' * 48))
####+++++++++++++++++++++++++++++++++++++++++++++++++++
###20190415#####################
###列表:属于容器类型
# from random import randint
# alist1 = [randint(1,100) for i in range(10)]
# print(alist1)            #[21, 88, 62, 5, 91, 85, 40, 45, 36, 7]
#
# alist = [21, 88, 62, 5, 91, 85,]
# print(alist.append(30)) #None
# print(alist)            #[21, 88, 62, 5, 91, 85, 30]
# print(alist.count(21))  #输出1,统计21在列表中出现的次数
# print(alist.index(21))  #输出0 统计21在列表中的下标
#
# alist.insert(5,101)     #在列表中下标为5的位置插入101
# print(alist)            #[21, 88, 62, 5, 91, 101, 85, 30]
#
# alist.reverse()
# print(alist)            #[30, 85, 101, 91, 5, 62, 88, 21]
#
# alist.sort()
# print(alist)            #[5, 21, 30, 62, 85, 88, 91, 101]
#
# alist.remove(30)
# print(alist)            #[5, 21, 62, 85, 88, 91, 101]
#
# alist.pop()
# print(alist)            #[5, 21, 62, 85, 88, 91]
# alist.pop(2)
# print(alist)            #[5, 21, 85, 88, 91]
#
# blist = alist.copy()    #将alist拷贝给blist
# print(blist)            #[5, 21, 85, 88, 91]
# clist = alist           #clist 与 alist 使用相同的地址符
# print(clist)            #[5, 21, 85, 88, 91]
#
# alist.extend(clist)     #将clist的内容汇入到alist
# print(alist)            #[5, 21, 85, 88, 91, 5, 21, 85, 88, 91]
# alist.clear()           #清空列表
# print(alist)            #[]

####元组###########
# a = (10)
# print(type(a))          #<class 'int'>  说明a是个int整数
# print(a)                #10
#
# b = (10,)
# print(type(b))          #<class 'tuple'> 说明b是个元组
# print(b)                #(10,)

###写一个栈程序########################################
#栈结构,类似于堆叠盘子,先放上去的堆在下方,先拿的都是最后放上去的
# import random,sys
# list_a = []
#
# def push_it():      #进栈
#     print('压栈')                  #调试测试
#     itm = input('>').strip()    #定义输入
#     if itm:                     #如果itm为非空则执行下面
#         list_a.append(itm)
#
# def pop_it():       #出栈
#     print('出栈')
#     if list_a:                  #如过list_a列表为非空,
#         print('栈中弹出:%s' % list_a.pop())   #输出的同时,列表中弹出最后一项
#     else:
#         print('空栈,无内容弹出')
#
# def view_it():    #查询
#     print('\033[31;1m%s\033[0m' % list_a)
#
# def show_menu():    #选择菜单
#     prompt = '''0:压栈
# 1:出栈
# 2:查询
# 3:退出
# 请选择相应的操作(0/1/2/3):'''
#     while True:
#         xz_1 = (input(prompt).strip()[0])
#         if xz_1 not in ['0','1','2','3']:
#             print('无效,请重新输入')
#             continue
#         elif xz_1=='0':
#             push_it()
#         elif xz_1=='1':
#             pop_it()
#         elif xz_1=='2':
#             view_it()
#         else:
#             print('退出')
#             break
#
# if __name__ == '__main__':      #主程序
#     show_menu()
#
# ###
# ##写一个栈程序,字典方式##########################
# 栈结构,类似于堆叠盘子,先放上去的堆在下方,先拿的都是最后放上去的
# import random,sys
# list_a = []
#
# def push_it():      #进栈
#     print('压栈')                  #调试测试
#     itm = input('>').strip()    #定义输入
#     if itm:                     #如果itm为非空则执行下面
#         list_a.append(itm)
#
# def pop_it():       #出栈
#     print('出栈')
#     if list_a:                  #如过list_a列表为非空,
#         print('栈中弹出:%s' % list_a.pop())   #输出的同时,列表中弹出最后一项
#     else:
#         print('空栈,无内容弹出')
#
# def view_it():    #查询
#     print('\033[31;1m%s\033[0m' % list_a)
#
# def show_menu():    #选择菜单
#     cmds = {'0':push_it,'1':pop_it,'2':view_it}
#     #采用字典方式:注意字典中函数名后不要加(),因为是把函数存入字典,
#     #并不是将函数结果存入字典,
#     prompt = '''0:压栈
# 1:出栈
# 2:查询
# 3:退出
# 请选择相应的操作(0/1/2/3):'''
#     while True:
#         # xz_1 = (input(prompt).strip()[0]) #删除用户输入的两端空格,并取出第一个
#         # if xz_1 not in ['0','1','2','3']:
#         #     print('无效,请重新输入')
#         #     continue
#         # elif xz_1=='0':
#         #     push_it()
#         # elif xz_1=='1':
#         #     pop_it()
#         # elif xz_1=='2':
#         #     view_it()
#         # else:
#         #     print('退出')
#         #     break
#         choice = input(prompt).strip()[0]   #删除用户输入的两端空格,并取出第一个
#         if choice not in  ['0','1','2','3']:
#             print('无效,请重试:')
#             continue
#         if choice == '3':
#             print('退出')
#             break
#         cmds[choice]()      #在字典中取出出入的数字对应的函数,加上后面的函数,即为调用函数
#
# if __name__ == '__main__':      #主程序
#     show_menu()

####字典######################
###1创建字典
# adict = dict(['ab',['name','tom'],('age',22)])
# print(adict)
# #dict的参数是个序列对象,序列中有三项,每一项又有两个项目,第一个项目是key,第二个是value
# bdict = {}.fromkeys(['tom','jerry','bob'],7)
# print(bdict)
###2访问字典
# adict = dict(['ab',['name','tom'],('age',22)])
# print(adict)
# for key in adict:
#     print('%s : %s' % (key,adict[key]))
# print(adict['name'])        #tom
#
# print('tom' in adict)           #False
# print('name' in adict)          #True


# ##3更新字典
# 字典的kye都是唯一的,不重复的,字典的key必须是不可变类型
# adict = dict(['ab',['name','tom'],('age',22)])
# adict['name'] = 'jerry'
# adict['zdd'] = '123456'
# print(adict)                #{'a': 'b', 'name': 'jerry', 'age': 22}


###4字典方法
# adict = dict(['ab',['name','tom'],('age',22)])
# print(adict.get('name', 'not found'))       #字典中有key,返回tom
# a = adict.get('qq')             #字典中没有key为qq项,返回值None给a
# print(a)                        #None
# adict.get('qq','not found')     #字典中没有kye为qq项,返回值None
# print(adict.get('qq','not found'))  #not found
#
# adict = dict(['ab',['name','tom'],('age',22)])
# b = adict.keys()                #返回adict字典中所有的key
# print(b)                        #dict_keys(['a', 'name', 'age'])
# print(adict.keys())             #dict_keys(['a', 'name', 'age'])
#
# adict = dict(['ab',['name','tom'],('age',22)])
# print(adict)                        #{'a': 'b', 'name': 'tom', 'age': 22}
# print(adict.values())               #dict_values(['b', 'tom', 22])  返回所有的value
#
#
# adict = dict(['ab',['name','tom'],('age',22)])
# print(adict)            #{'a': 'b', 'name': 'tom', 'age': 22}
# print(adict.items())    #dict_items([('a', 'b'), ('name', 'tom'), ('age', 22)])返回所有的(key,value)组成的集合
#
# adict = dict(['ab',['name','tom'],('age',22)])
# print(adict)                    #{'a': 'b', 'name': 'tom', 'age': 22}
# print(adict.pop('a'))           #b            #弹出key是a的项

#####模拟用用户登录系统
# import getpass
#
# userdb = {}
# print(userdb)
#
# def new():
#     print('正在注册')
#     user = input('请输入新用户名').strip()
#     if user and user not in userdb:
#         passwd = input('密码:')
#         userdb[user] = passwd
#
# def old():
#     print('正在登录')
#     user = input('请输入用户名:').strip()
#     passwd = getpass.getpass('密码:')     #定义输入的密码,且是不明文显示
#     if userdb.get(user) == passwd:
#                 #如果输入的用户不在userdb字典中,返回值将是None不会等于刚刚输入的密码
#                 #或者用户存在,返回的value值不等于,刚刚输入的passwd,都不执行下面
#         print('登录成功')
#     else:
#         print('登录失败')
#
# def menu():
#     cmds = {'0':new,'1':old}
#     xz='''0:新用户注册
# 1:老用户登录
# 2:退出
# 请选择(0/1):'''
#     while True:
#         choice = input(xz).strip()
#         if choice not in ['0','1','2']:
#             print('请重新选择')
#             continue
#         if choice == '2':
#             print('退出')
#             break
#         cmds [choice]()
#
# if __name__ == '__main__':
#     menu()

#####linux与windows文件的转换
##windows文本文件的行结束标志是\r\n
##类unix文本本间的行结束标志是\n

#编写程序,将unix文本文件格式转换为Windows文本文件格式
###uninx2dos的转换程序
# import sys
#
# def unix2dos(fname):                #接收位置参数
#     dst_fname = fname + '.txt'      #重命名
#
#     with open(fname) as src_fobj:               #打开源文件
#         with open(dst_fname,'w') as dst_fobj:   #以w方式打开目标文件,没有则创建
#             for line in src_fobj:               #遍历源文件
#                 line = line.rstrip() + '\t\n'   #重新获取line内容,去掉右边的空格,加上\t\n
#                 dst_fobj.write(line)            #将line内容重新写入目标文件
#
# if __name__ == '__main__':
#     unix2dos(sys.argv[1])       #位置参数

###
# [root@room9pc01 python]# python3
# >>> f = open('/root/桌面/python/gen_pass.py.txt')
# >>> f.readline()
# '#! /usr/bin/env python\n'                #转换之前是\n结尾

# [root@room9pc01 python]# python3 dayall.py gen_pass.py
# [root@room9pc01 python]# ls                                   #转换后多了gen_pass.py.txt 文件
# dayall.py  gen_pass.py  gen_pass.py.txt  home-100.py  Python-3.7.3.tgz
# [root@room9pc01 python]# python3
# >>> f = open('/root/桌面/python/gen_pass.py.txt')
# >>> f.readline()
# '#! /usr/bin/env python\t\n'              #转换后是\t\n结尾了

##########
###编写类似进度条程序##
# import time
# n = 0
# print('#' * 20, end='')
# while True:
#     print('\r%s@@@%s' % ('#' * n ,  '#' * (19 - n)),end='')
#     n +=1
#     if n == 20:
#         n = 0
#     time.sleep(0.3)

######集合
#由不同元素构成,元素必须是不可变对象
#常用来去重
#用{}表示,像是一个无值的字典,只有key
# from random import randint
# alist = [randint(1, 20) for i in range (10)]
# print(alist)            #十个1到20之间的随机数[13, 19, 12, 4, 20, 5, 13, 8, 16, 16]
# aset = set(alist)
# print(aset)         #按序排列,并去重{4, 5, 8, 12, 13, 16, 19, 20}
#
# aset = set('abc')
# print(aset)            #{'b', 'a', 'c'}
# bset = set('bcd')
# print(bset)             #{'c', 'd', 'b'}
#
# print(aset|bset)        #并集{'b', 'c', 'a', 'd'}
# print(aset&bset)        #交集{'b', 'c'}
# print(aset-bset)        #差集{'a'}   aset中有,bset中没有
#
# print(aset.add('abc'))      #None  不能这么显示
# aset.add('abc')
# print(aset)                 #先添加在打印{'a', 'c', 'b', 'abc'}
#
# #批量添加,删除
# aset = set('abc')
# print(aset)            #{'b', 'a', 'c'}
# aset.update('xyz')      #批量添加元素
# print(aset)             #{'a', 'z', 'b', 'c', 'x', 'y'}
# aset.update(['xxx','yyy','zzz'])
# print(aset)             #{'z', 'x', 'c', 'b', 'a', 'y', 'xxx', 'zzz', 'yyy'}
# aset.remove('zzz')
# print(aset)             #{'xxx', 'c', 'yyy', 'x', 'b', 'z', 'y', 'a'}


#
# ###比较两个a,b两个文件,
# with open('/tmp/passwd1') as f1:
#     s1 = set(f1)
#
# with open('/tmp/passwd2') as f2:
#     s2 = set(f2)
#
# s3 = s2 - s1
#
# with open('/tmp/result.txt','w') as f3:
#     f3.writelines(s3)
#
# ###实际操作
# #passwd1文件内容
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# adm:x:3:4:adm:/var/adm:/sbin/nologin
# lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
# sync:x:5:0:sync:/sbin:/bin/sync
# #passswd2文件内容
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# adm:x:3:4:adm:/var/adm:/sbin/nologin
# ni hao a
# lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
# sync:x:5:0:sync:/sbin:/bin/sync
# root:x:0:0:root:/root:/bin/bash
# zdd
# bin:x:1:1:bin:/bin:/sbin/nologin
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# adm:x:3:4:adm:/var/adm:/sbin/nologin
# lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
# sync:x:5:0:sync:/sbin:/bin/sync
# roooasdft:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# adm:x:3:4:adm:/var/adm:/sbin/nologin
# lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
# sync:x:5:0:sync:/sbin:/bin/sync
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# adm:x:3:4:adm:/var/adm:/sbin/nologin
# lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
# sync:x:5:0:sync:/sbin:/bin/sync

#程序运行后产生的新文件内容
# [root@room9pc01 tmp]# cat result.txt
# roooasdft:x:0:0:root:/root:/bin/bash
# ni hao a
# zdd

###时间表示方式
##1,时间戳,距离1970-1-1 0:00:00 之间的秒数
# import time
# print(time.time())      #1555318981.2148066
# ##2,UTC时间:世界协调时
# print(time.ctime())        #Mon Apr 15 17:03:01 2019
# ##3,struct_time九元组
# print(time.localtime())
# #time.struct_time(tm_year=2019, tm_mon=4, tm_mday=15, tm_hour=17, tm_min=3, tm_sec=1, tm_wday=0, tm_yday=105, tm_isdst=0)
# t = time.localtime()
# a=(t.tm_year)
# print(a)            #2019
# print(t.tm_mon)     #4
# ##需要掌握的时间表示方式
# print(time.time())                          #时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S'))   #显示固定格式2019-04-15 16:56:07
# print(time.strptime('2019-04-15 16:56:07','%Y-%m-%d %H:%M:%S'))
#                                           #将时间字符串转换成struct_time样式(九元组)
# #时间比较
# t1 = time.strptime('2019-04-15 16:56:07','%Y-%m-%d %H:%M:%S')
# t2 = time.localtime()
# print(t1 > t2)
# print(t2 > t1)
#
# print(time.strftime('%a %A'))       #
#
# time.sleep(3)           #时间睡眠

###datetime
# import datetime
# t1 = datetime.datetime.now()              #年月日时分秒毫秒
# t2 = datetime.datetime(2019, 4, 10)
# print(t1)                                 #2019-04-15 17:13:02.111975
# print(t2)                                 #2019-04-10 00:00:00
# print(t1 > t2)          #True
#
# days = datetime.timedelta(days=100,hours=10)
# print(t1 - days)                #100天零10十小时之前的时间2019-01-05 07:13:02.111975
# print(t1 + days)                #100天零10小时之后的时间2019-07-25 03:13:02.111975

#######异常处理##################
# 错误代码
# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError,ZeroDivisionError):   #字母无法转换成整数.多个错误情况放一起必须加括号
#     print('滚蛋,无效的数字1')
# # except ZeroDivisionError:       #0无法作为被除数
# #     print('滚犊子,无效的数字2')
# except KeyboardInterrupt:       #ctrl+c
#     print('\n拜拜了您勒')
#     exit()                      #程序遇到exit就会退出,后续代码不执行
# except EOFError:                #ctrl+D
#     print('\n会不会用?不会滚蛋')
#     exit()
# else:
#     print(result)               #输出结果
# finally:                        #不管程序是否发生异常,都会执行
#     print('Done')

######触发异常#####
# def set_age(name, age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超出范围')
#     print('%s is %s years old.' % (name, age))
#
# def set_age2(name, age):
#     assert 0 < age < 120, '年龄超出范围'  # 如果age不在此范围，一定发生AssertionError
#     print('%s is %s years old.' % (name, age))
#
# if __name__ == '__main__':
#     set_age2('杨晨', 24)

#####OS模块


###pickle模块

###记账本程序
# import time,os,pickle
#
# def sr():           #经过cmkds[xz_2](fname)传参fname到这
#     print('sr')
#     amount = int(input('收入金额:'))
#     comment = input('说明')
#     date = time.strftime('%Y-%m-%d')    #获取当前日期
#     with open(fnam,'rb') as fobj:
#         data = pickle.load(fobj)            #从文件中取出全部记录
#         balance = data[-1][-2] + amount     #文件最后一行的倒数第2项是余额
#
#     line = [date,amount,0,balance,comment]
#     data.apend(line)                        #把最新记录加入到大列表中
#
#     with open(fname,'wb') as fobj:
#         pickle.dump(data,fobj)              # 把大列表写到文件
#
#
# def zc():
#     print('zc')
#
# def cx():
#     print(cx)
#
# def show_menu():
#     xz_1 = '''0:收入
# 1:支出
# 2:查询
# 3:退出
# 请选择相应操作:'''
#     cmds = {'0': sr, '1': zc, '2': cx}
#
#     fname = 'jzb.data'
#     if not os.path.exists(fname):
#         date = time.strftime('%Y-%m-%d')
#         data = [
#             [ date,0,0,10000,'init data']
#         ]
#         with open(fname,'wb') as fobj:
#             pickle.dump(data,fobj)
#
#     while True:
#
#         xz_2 = input(xz_1).strip()
#         if xz_2 == '3':
#             print('选择了退出')
#             exit()
#
#         if xz_2 not in ['0','1','2']:
#             print('无效输入')
#
#         cmkds[xz_2](fname)
#
# if __name__ == '__main__':
#     show_menu()

##函数
# def myfunc(name, age=23):
#     pass
# #函数中的name就被称作位置参数，age被称作关键字参数
#
# def get_info(name, age):
#     print('%s is %s years old' % (name, age))
# #get_info()                                  # error，参数个数不足
# #get_info('tom', 20, 30)                     # error, 参数个数太多
# get_info('tom', 20)                         # OK
# get_info(20, 'tom')                         # OK，但是语义不对
# get_info(age=20, name='tom')                # OK
# #get_info(age=20, 'tom')                     # error, 位置参数必须在关键字参数前
# #get_info(20, name='tom')                    # error, name得到了多个值
# get_info('tom', age=20)                     # OK

##函数参数组
# def func1(*args): #args前面的一个*号,表明args是元组,传参会把参数放入元组
#     print(args)
#
# def func2(**kwargs):  #kwargs前面两个**号,表名kwargs是字典
#     print(kwargs)
#
# if __name__ == '__main__':
#     func1()
#     func1('hao')
#     func1('zdd',123)
#     func2()
#     func2(name='tom',age=20)

##加*号
# print('abc')
# print(*'abc')
# ##print(**'abc')            #错误
# print(*[10,20,30])
# print(*(10,20,30))


##字典加两个**号
# def info(name,age):
#     print('%s:%s' % (name,age))
#
# if __name__ == '__main__':
#     info(**{'name':'tom','age':20})
#
# info(name='tom',age=20)

# ###简单的加减法数学游戏
# import random
#
# def sf():
#     nums = [random.randint(1,100) for i in range(2)]
#     nums.sort(reverse=True)         #降序排列,默认升序
#     op = random.choice('+-')
#     a = 0
#     while a < 3:
#         a += 1
#         if op == '+':
#             result = nums[0] + nums[1]
#         else:
#             result = nums[0] - nums[1]
#
#         prompt = '%s %s %s = ' % (nums[0], op , nums[1])
#         answer = int(input(prompt))
#
#         if answer == result:
#             print('对')
#             break
#         else:
#             print('错')
#     print('结果是:%s' % result)
# def main():
#     while True:
#         print('开始测智商了')
#         sf()
#         y_n = input('请选择是否继续(y/n)?').strip()[0]
#         if y_n in 'nN':
#             print('\n测试结束')
#             break
#
# if __name__ == '__main__':
#     main()

#
# ###简单的加减法数学游戏:增加了错误收集try
# import random
#
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
#
# def exam():
#     cmds = {'+':add,'-':sub}        #定义函数选择字典
#     nums = [random.randint(1,100) for i in range(2)]    #随机生成两个数
#     nums.sort(reverse=True)                             #重新排列,默认升序,这是降序
#     op = random.choice('+-')                            #随机选择是+法还是-法
#     result = cmds[op](*nums)                #将列表拆开,传参到add函数或者sub函数,进行运算
#     prompt = '%s %s %s = ' % (nums[0],op,nums[1])   #固定格式,第一个数 +/- 第二个数 =
#     counter = 0                                     #用作循环次数计数
#
#     while counter < 3:
#         try:
#             answer = int(input(prompt)) #用户输入答案时捕获错误
#         except:                         #捕获所有错误操作,不按程序答对,或者答错三次不结束,不推荐
#             print('非法操作,请继续')
#             continue
#
#         if answer == result:            #如果输入的等于运算返回的结果
#             print('答对了')
#             break
#         print('不对哦')                  #如果输入的不等于算返回的结果,则执行
#         counter +=1
#     else:
#         print('%s%s' % (prompt,result))  #输出上面的固定格式和结果
#
# def main():
#     while True:
#         print('开始测智商了')
#         exam()                          #调用函数
#         try:
#             y_n = input('请选择是否继续(y/n)?').strip()[0] #输入是否继续时捕获错误
#         except IndexError:
#             continue
#         except (KeyboardInterrupt,EOFError):    #ctrl+c 与 ctrl+d 的错误
#             y_n = 'n'
#
#         if y_n in 'nN':
#             print('\n测试结束')
#             break
#
# if __name__ == '__main__':
#     main()

####匿名函数####################

###简单的加减法数学游戏--匿名函数lambda方式
# import random
#
# def exam():
#     cmds = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y}     #用匿名函数代替运算
#     nums = [random.randint(1,100) for i in range(2)]    #随机生成两个数
#     nums.sort(reverse=True)                             #重新排列,默认升序,这是降序
#     op = random.choice('+-*')                            #随机选择是+法还是-法
#     result = cmds[op](*nums)                #将列表拆开,传参到add函数或者sub函数,进行运算
#     prompt = '%s %s %s = ' % (nums[0],op,nums[1])   #固定格式,第一个数 +/- 第二个数 =
#     counter = 0                                     #用作循环次数计数
#
#     while counter < 3:
#         try:
#             answer = int(input(prompt)) #用户输入答案时捕获错误
#         except:                         #捕获所有错误操作,不按程序答对,或者答错三次不结束,不推荐
#             print('非法操作,请继续')
#             continue
#
#         if answer == result:            #如果输入的等于运算返回的结果
#             print('答对了')
#             break
#         print('不对哦')                  #如果输入的不等于算返回的结果,则执行
#         counter +=1
#     else:
#         print('%s%s' % (prompt,result))  #输出上面的固定格式和结果
#
# def main():
#     while True:
#         print('开始测智商了')
#         exam()                          #调用函数
#         try:
#             y_n = input('请选择是否继续(y/n)?').strip()[0] #输入是否继续时捕获错误
#         except IndexError:
#             continue
#         except (KeyboardInterrupt,EOFError):    #ctrl+c 与 ctrl+d 的错误
#             y_n = 'n'
#
#         if y_n in 'nN':
#             print('\n测试结束')
#             break
#
# if __name__ == '__main__':
#     main()

#####filter函数(高阶函数)
# from random import randint
#
# def func1(x):
#     return x % 2
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#
#     result = filter(func1,nums)
#     print(list(result))
#
#     result2 = filter(lambda x: x % 2,nums)
#     print(list(result2))
#
#     result3 = filter(lambda x: not x % 2,nums)
#     print(list(result3))


#############################
####map函数
# from random import randint
#
# def func1(x):
#     return x + 2
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#
#     result = map(func1,nums)     #将nums中的每个数字交给func1函数进行加工,返回结果
#     print(list(result))
#
#     result2 = map(lambda x: x + 2, nums)  #将nums中的每个数字交给lambda函数进行加工,返回结果
#     print(list(result2))
#
# #输出结果:
# [80, 1, 61, 44, 28, 37, 47, 39, 61, 83]
# [82, 3, 63, 46, 30, 39, 49, 41, 63, 85]
# [82, 3, 63, 46, 30, 39, 49, 41, 63, 85]

##############################################################################
#########函数高级应用
###全局变量,局部变量,global
# x = 10
# def foo():
#     print(x)
# foo()
#
# def foo2():
#     x = 'hello'        #局部变量也有变量x,它将会把全局变量x在此函数中遮盖住
#     print(x)           #输出hello
# foo2()
# print(x)               #输出10
#
#
# def foo3():
#     global x             #声明x为全局变量,将会覆盖之前的全局变量
#     x = 10000
#     print(x)            #输出:10000
# foo3()
# print(x)                 #输出:10000

####名字空间####

# i = 1
#
# def f():
#     i = 2
#     def g():
#         print(i)
#     return g
#
#
# func = f()
# func()
# print(i)


###偏函数#####改造现有函数,生成新函数   待补充
###partial
# from functools import partial
#
# def add(a,b,c,d,e):
#     return a + b + c + d + e
# a = add(10,20,30,40,5)
# # print(a)
#
# myadd = partial(add,10,20,30,40)
# # print(myadd)
# b = myadd(5)
# print(b)
#
####简单GUI程序####简单测试
# import tkinter
# from functools import partial
# window = tkinter.Tk()
# lb = tkinter.Label(window, text="Hello World!", font="Arial 20")
# # b1 = tkinter.Button(window, fg='white', bg='blue', text='Button 1')
# MyButton = partial(tkinter.Button, window, fg='white', bg='blue')
# b1 = MyButton(text='Button 1')
# b2 = MyButton(text='Button 1')
# b3 = MyButton(text='Button 1')
# qb = MyButton(text='QUIT', command=window.quit)
#
# lb.pack()
# b1.pack()
# b2.pack()
# qb.pack()
##################################################################################
# import time
# a = time.strftime('%Y')
# print(a)
#
######################20190417
###递归函数
# def func1(x):
#     if x == 1:
#         return 1
#     return x * func1(x - 1)
# if __name__ == '__main__':
#     print(func1(5))
###快速排序函数
# from random import randint
#
# def paixu(item):
#     if len(item) < 2:
#         return item
#
#     px_zj = item[0]
#     px_zx = []              #比列表第一个数小的放到这个集合
#     px_zd = []              #比列表第一个数打的放到这个集合
#
#     for a in item[1:]:      #从列表第二个数开始遍历
#         if a <= px_zj:
#             px_zx.append(a)          #把比第一个数小的添加到px_zx列表
#         else:
#             px_zd.append(a)          #把比第一个数大的添加到px_zd列表
#
#     return paixu(px_zx) + [px_zj] + paixu(px_zd)
#
# if __name__ == '__main__':
#
#     nums = [randint(1,100) for i in range(10)]
#     print(nums)
#     print(paixu(nums))          #调用函数,并将nums列表传参给item

#####################################################################
####生成器
# def my_gen():
#     yield 'hello world'
#     num = 10 + 5
#     yield num
#     yield 100
#     yield 1
#
# if __name__ == '__main__':
#     my_gen()
#
# a = my_gen()
#
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# # print(a.__next__())         #报错,只定义了4个生成器
# print()                       #空格
# mg = my_gen()
# for i in mg:                #实际使用中使用for循环
#     print(i)


#######################################################################
###内部函数,闭包(了解)

# def deco(func):
#     def red():
#         return '\033[31;1m%s\033[0m' % func()
#     return red
#
# def hello():
#     return 'hello world!'
#
# def greet():
#     return '你好'
#
# if __name__ == '__main__':
#     print(hello())      #普通调用
#
#     a = deco(hello)     #将hello函数作为参数传递给deco ,deco的返回值是red函数
#     print(a())          #调用 a 函数,实际上是调用red函数

# ####内部函数,装饰器(了解)
# def deco(func):
#     def red():
#         return '\033[31;1m%s\033[0m' % func()
#     return red
#
# def hello():
#     return 'hello world!'
#
# @deco                     #装饰器
# def greet():
#     return '你好'
#
# if __name__ == '__main__':
#     # print(hello())      #普通调用
#
#     a = deco(hello)     #将hello函数作为参数传递给deco ,deco的返回值是red函数
#     print(a())          #调用 a 函数,实际上是调用red函数
#
#     print(greet())


###模块
#
# import sys
# print(sys.path)             #模块导入的时候,将会在sys.path定义的位置下搜索模块
#
#
# ##模块导入
# import time
# import os,sys                               #不推荐使用
# from random import random,choice,randint
# import pickle as p                          #导入的同时,给模块起别名
#
# ###包
# def pstar():
#     print('*' * 30)
#
# import  mypace.hi
#
# ##相对导入模块
# ##绝对导入模块


##########内置模块
###hashlib模块
###输入文件名,生成md5哈希值的程序
# import hashlib
# import sys,pickle
#
# def ahash(fname):
#
#     m = hashlib.md5()               #创建文件
#
#     with open(fname,'rb') as fobj:
#         while True:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)          #更新
#
#     return m.hexdigest()            #输出
#
#
# if __name__ == '__main__':
#
#     try:
#         f = sys.argv[1]
#         print(ahash(f))
#     except IndexError:
#         print('错误,请输入需要检测的文件名')
#     except (FileNotFoundError,NameError):
#         print('请输入正确的文件名')

#############################################################
###tarfile模块
# import os
# import tarfile
#
# os.chdir('/etc')                                        #进入目录
# os.mkdir('/pythonbackup')                                 #创建目录
# tar = tarfile.open('/pythonbackup/mytest.tar.gz','w:gz')
#                                     #开始使用gzip压缩.以w方式,会创建一个mytest.tar.ge文件,pythontest目录需提前创建
# tar.add('hosts')                                        #添加入要压缩的文件绝对路径
# tar.add('/etc/hosts')                                   #绝对路径,会目录结果一起打包
# tar.add('security')                                     #继续添加(这是目录)
# tar.close()
#
# #以上是压缩文件的全部步骤,以下是解压缩的全部过程
#
# tar = tarfile.open('/pythonbackup/mytest.tar.gz','r:gz')     #打开之前创建tar包,以r的方式
# tar.extractall('/pythonbackup/mydemo')                           #解压缩到指定目录,目录没有则会创建
# tar.close()

###############################################################
###具有完全备份和增量备份的程序
# from time import strftime
# import os
# import tarfile
# from check_md5 import check_md5
# import pickle

#定义全量备份函数
# def full_backup(src,dst,md5file):
#
#     #给完全备份的tar包命名
#     # fname = os.path.basename(src)          #只获取目标的文件名,可结合到下面一条语句了
#     fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))    #取名
#     fname = os.path.join(dst,fname)          #将备份的tar包名拼接绝对路径
#
#     #打包文件
#     tar = tarfile.open(fname,'w:gz')        #打包开始
#     tar.add(src)                            #添加要打包的文件
#     tar.close()
#
#     #计算每个文件的md5值
#     md5dict = {}                                #准备用来存放哈希值的列表
#     for path, folders, files in os.walk(src):   #os.walk方式来获取文件路径和文件名,遍历元组,详情请看walk的详解
#         for file in files:                      #再遍历得到的所有文件名
#             key = os.path.join(path, file)      #拼接所有文件的路径/文件名
#             md5dict[key] = check_md5(key)       #经过check_md5程序产生的哈希值赋值给字典md5dict
#                                                 #自编写的check_md5模块必须与本程序文件放同一目录,该模块作用是生成哈希值
#     #将字典写入文件
#     with open(md5file,'wb') as fobj:            #以wb方式打开md5file指定的文件,没有则创建
#         pickle.dump(md5dict,fobj)               #pickle是能将任何内容存入文件中,将字典mdict的内容写入md5file中
#
# def incr_backup(src,dst,md5file):
#
#     #给备份的tar包命名
#     # fname = os.path.basename(src)
#     fname = '%s_incr_%s.tar.gz' % (os.path.basename(src),strftime('%Y%m%d'))
#     fname = os.path.join(dst,fname)
#
#     #计算每个文件的md5值
#     md5dict = {}            #将用来装哈希值
#     for path , folders, files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5dict[key] = check_md5(key)
#
#     # 取出前一天的md5字典
#     with open(md5file,'rb') as fobj:
#         old_md5 = pickle.load(fobj)
#
#     # 更新md5字典文件
#     with open(md5file,'wb') as fobj:
#         pickle.dump(md5dict,fobj)
#
#     tar = tarfile.open(fname,'w:gz')
#     for key in md5dict:           #遍历md5dict字典,返回key值,key就是文件名，value是md5值
#         if md5dict[key] != old_md5.get(key):  #字典名[key],返回的是value，字典名.get(key)有key返回value,无key返回flase
#             tar.add(key)           #key返回的是文件名，就添加到tar包中
#     tar.close()
#
# if __name__ == '__main__':
#     src = '/pythonbackup/mydemo/security'        #定义要备份的源目录
#     dst = '/pythonbackup/demo'                   #定义放备份文件的目录
#
#     md5file = '/pythonbackup/demo/md5.data'     #定义校验目录
#     if strftime('%a') == 'Mon':                 #判断是不是星期三
#         full_backup(src,dst,md5file)            #调用全量备份函数
#     else:
#         incr_backup(src,dst,md5file)            #调用增量备份函数
#

#########################################################################################################
# adict = dict(['ab',['name','tom'],('age',22)])
#
# # print(adict)
#
# for key in adict:
#     # print(key)
#     print(adict[key])
#     # print(adict.get(key))
#

######pop简介#######################20190418##################################################

###类基本概念

###构造器方法创建类

# class Warriot:
#     def __init__(self,name,weapon): #_init_是构造器方法,当实例化时自动调用,不是必需的
#         self.name = name
#         self.weapon = weapon
#
# if __name__ == '__main__':
#     lb = Warriot('吕布','方天画戟')  #lb实例,自动调用_init_ .lb 与 self 对应,吕布与name对应,方天画戟与weapon对应
#     zdd = Warriot('zdd','杀猪刀')
#     print('%-8s   %s' % (lb.name , lb.weapon))
#     print('%-8s   %s' % (lb.name, zdd.weapon))
#     print('%-8s   %s' % (zdd.name , lb.weapon))

#实例化时,实例自动作为第一个参数传递给_init_方法
#self只是一个变量名,名字也可以是其他名字,python中习惯起名self
#拥有self(绑定到实例的属性),


###其他绑定方法##########

# class Warriot:
#     def __init__(self,name,weapon): #_init_初始化实例属性,构造器方法,当实例化时自动调用
#         self.name = name
#         self.weapon = weapon
#
#     def speak(self,content):        #创建类中函数,叫做方法,设置content参数
#         print('%s: 我手持%s, %s' % (self.name, self.weapon, content))
#
# if __name__ == '__main__':
#     lb = Warriot('吕布','方天画戟')  #lb实例,自动调用_init_ .lb 与 self 对应,吕布与name对应,方天画戟与weapon对应
#     zdd = Warriot('zdd','杀猪刀')
#     print(lb.name , lb.weapon)      #吕布 方天画戟
#     print(zdd.name, zdd.weapon)     #zdd 杀猪刀
#     print()
#
#     lb.speak('人在塔在')                                #调用speak方法,并传参给content
#     zdd.speak('%s你就是渣渣,老子拔你网线' % lb.name)
#     lb.speak('......')

# ###实际输出
# 吕布 方天画戟
# zdd 杀猪刀
#
# 吕布: 我手持方天画戟, 人在塔在
# zdd: 我手持杀猪刀, 吕布你就是渣渣,老子拔你网线
# 吕布: 我手持方天画戟, ......


#############################################################################
# class Warrior:
#     def __init__(self,name,weapon): #_init_初始化实例属性,构造器方法,当实例化时自动调用
#         self.name = name
#         self.weapon = weapon
#
#
#     def speak(self,content):        #创建类中函数,方法,设置content参数
#         print('%s: 我手持%s, %s' % (self.name, self.weapon, content))
#
#
# if __name__ == '__main__':
#     lb = Warrior('吕布','方天画戟')  #lb实例,自动调用_init_ .lb 与 self 对应,吕布与name对应,方天画戟与weapon对应
#     zdd = Warriot('zdd','杀猪刀')
#     print('%-8s   %s' % (lb.name , lb.weapon))
#     print('%-9s   %s' % (zdd.name, zdd.weapon))
#     print()
#
#     lb.speak('人在塔在')                                #调用speak方法,并传参给content
#     zdd.speak('%s你就是渣渣,老子拔你网线' % lb.name)
#     lb.speak('......')


###组合和派生
#两个不同的类,一个类是另一个类的组件
##老师代码game2.py
# class Weapon:
#     def __init__(self, name, strength):
#         self.name = name
#         self.strength = strength
#
# class Warrior:
#     def __init__(self,name,weapon): #_init_初始化实例属性,构造器方法,当实例化时自动调用
#         self.name = name
#         self.weapon = weapon    #weapon参数接收的是Weapon('方天画戟',100),所以又调用上面的Weapon方法
#
#     def speak(self,content):        #创建类中函数,方法,设置content参数
#         print('%s: 我手持%s, %s' % (self.name, self.weapon, content))
#
# if __name__ == '__main__':
#     w = Weapon('方天画戟',100)
#     print(w.name,w.strength)        #输出:方天画戟 100
#
#     lb = Warrior('吕布',  w)        #lb实例,传参为weapon是传的'吕布和Weapon('方天画戟',100)'
#     # print(lb.weapon)
#     print(lb.weapon.name,  lb.weapon.strength)      #输出:方天画戟 100

##########上面的代码进化成下面(老师代码game3.py)
#
# class Weapon:
#     def __init__(self, name, strength):
#         self.name = name
#         self.strength = strength
#
# class Warrior:
#     def __init__(self,name,wname,wstrength):  #修改地方
#         self.name = name
#         self.weapon = Weapon(wname,wstrength)   #修改地方,wname,wstrength传给上面Weapon方法
#
#     def speak(self,content):        #创建类中函数,方法,设置content参数
#         print('%s: 我手持%s, %s' % (self.name, self.weapon, content))
#
# if __name__ == '__main__':
#     lb = Warrior('吕布','方天画戟', 100)
#     print(lb.weapon)                                #输出:<__main__.Weapon object at 0x7fc0c3ae87f0>是对象
#     print(lb.name, lb.weapon.name,  lb.weapon.strength)      #输出:吕布 方天画戟 100

# ###组合:
#两个不同的类,一个类是另一个类的组件
#子类继承父类
####老师game4.py#子类与父类###########################
# class Warrior:
#     def __init__(self,name,weapon): #_init_初始化实例属性,构造器方法,当实例化时自动调用
#         self.name = name
#         self.weapon = weapon
#
#
#     def speak(self,content):        #创建类中函数,方法,设置content参数
#         print('%s: 我手持%s, %s' % (self.name, self.weapon, content))
#
#
# class MaleWarriot(Warrior):         #括号中指定父类(基类),MaleWarriot子类继承了父类所有属性
#     def attcck(self):
#         print('attack(攻击)')
#
#
# if __name__ == '__main__':
#     lb = MaleWarriot('吕布','方天画戟')
#     print(lb.name , lb.weapon)      #输出吕布 方天画戟
#
#     lb.speak('aaa')         #输出:  吕布: 我手持方天画戟, aaa,先子类MaleWarriot中,找speak方法,找不到就到父类去找
#
#     lb.attcck()             #输出:attack(攻击)  子类拥有父类与子类的所有功能

########myclass######################################
#
# class A:
#     def func1(self):
#         print('a func')
#
#     def func(self):
#         print('aaaaaaaa')
#
# class B:
#     def func2(self):
#         print('b func')
#
#     def func(self):
#         print('BBBBBBBBBB')
#
# class C(B, A):  # 父类可以有多个
#     def func3(self):
#         print('c func')
#
#     def func(self):
#         print('CCCCCCCCCCC')
#
# if __name__ == '__main__':
#     c1 = C()         # c1具有ABC三个类的方法
#     c1.func1()
#     c1.func2()
#     c1.func3()
#     c1.func()  # 同名方法查找的顺序是自下向上，自左向右
# #显示结果:
# # a func
# # b func
# # c func
# # CCCCCCCCCCC

############################################################
##出版商程序##
# magic魔法方法:指的是那些__xxxx__这样的方法
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '<%s>' % corepy.title
#
#     def __call__(self):
#         print('<%s> is written by %s ' % (self.title , self.author))
#
#
# if __name__ == '__main__':
#     corepy = Book('Python核心编程', 'Wesley')       #调用__init__方法
#     print(corepy)       #自动调用__str__方法,打印实例,                  输出:<Python核心编程>
#     corepy()            #自动调用__call__方法,使实例像函数一样,可以调用使用 输出:<Python核心编程> is written by Wesley

##显示结果
# <Python核心编程>
# <Python核心编程> is written by Wesley


# ####正则



#####re模块

import re
#match函数:从字符串开头开始匹配,匹配成功,则返回一个匹配对象,否则返回None
# a = re.match('f..','food')          #从头开始匹配,
# print(a)                            #输出:<_sre.SRE_Match object; span=(0, 3), match='foo'>
#
# b = re.match('f..','seafood')            #未匹配到,返回None
# print(b)                                 #输出:None

####search函数:在字符串中查找正则表达式模式的第一次出现,如果匹配成功,则返回一个匹配对象,否则返回None
# c = re.search('f..','seafood')  #搜索
# print(c.group())                #输出:foo   匹配对象的group方法获取匹配内容

##group方法:使用match或search匹配成功后,返回的匹配对象可以通过group方法获得匹配内容



####findall函数:在字符串中查找正则表达式模式的所有(非重复)出现,返回一个匹配对象的列表
# d = re.findall('f..','seafood')     #返回所有匹配内容的列表
# print(d)                            #输出:['foo'] --列表
#
# e = re.findall('f..','seafood is food')
# print(e)                                #输出:['foo', 'foo'] --列表


####finditer函数:和findall函数有相同的功能,但返回的不是列表而是迭代器,对于每个匹配,该迭代器返回一个匹配对象
# f = re.finditer('f..','seafood is food')    #返回的是由匹配对象构成的生成器
# print(f)                                #输出<callable_iterator object at 0x7f13b3b67630>
# for i in f:
#     print(i.group())
# 输出结果
# foo
# foo

###split方法:根据正则表达式中的分隔符把字符分隔为一个列表,并返回成功匹配的列表
###字符串也有类似的方法,但是正则表达式更加灵活
# g = re.split('-|\.' , 'hello-world.tar.ge')
# print(g)                            #输出:['hello', 'world', 'tar', 'ge']
#
#
# ####sub方法:把字符串中所有匹配正则表达式的地方替换成新的字符串
# h = re.sub('X','zdd','Hi X . How art you X')        #将目标里的X全部换成zdd
# print(h)                            #输出:Hi zdd . How art you zdd


###compile函数:对正则表达式模式进行编译,返回一个正则表达式对象
##不是必须要用这种方式,但是在大量匹配的情况下,可以提升效率
# i = re.search('f..' , 'seafood')
# print(i.group())
#
# patt = re.compile('f..')            #模式先编译,可提升效率,建议做法
# i = patt.search('seafood')          #编译后的对象也有search(返回第一个匹配)/findall(返回列表)等方法
# print(i.group())                    #输出:foo


##贪婪匹配: 默认情况下,* +总是尽量多的匹配
# # *  +和? 都是贪婪匹配操作符,在其后加上?可以取消其贪婪匹配行为
# # 正则表达式匹配对象通过groups函数获取子组

# j = re.search('.+(\d+)','his phone number is :15011223345')
# print(j.group())             #j.group总是匹配全部的模式.+(\d+)       #输出:his phone number is :15011223345
#
# print(j.group(1))                   #匹配第1个()中的内容
# print(j.group(2))                 #报错
# 说明:.+是贪婪匹配,它尽可能匹配更多,的内容，\d+至少需要一个数字，所以.+给\d+留了
#
##如果希望\d+能匹配更多的内容，使用?来取消贪婪匹配，让\d+匹配更多内容 如下
# k = re.search('.+?(\d+)' , 'his phone number is :15011223345')
# print(k.group())            #输出:his phone number is :15011223345
#
# print(k.group(1))           #输出:15011223345

###分析apache访问日志--函数方式
# import re
#
# def count_patt(fnam,patt):
#     patt_dict = {}
#     cpatt = re.compile(patt)        #编译,patt由参数传过来,ip或者br的正则
#     with open(fname) as fobj:       #打开文件
#         for line in fobj:           #遍历这个文件,获得每一行的内容
#             m = cpatt.search(line)  #经过上面编译后,在这search每一行,返回符合ip正则或者br正则
#             if m:                   # 如果匹配到内容，放到下面key变量，None表示False
#                 key = m.group()
#                 patt_dict[key] = patt_dict.get(key,0) + 1
#     return patt_dict
# #
# if __name__ == '__main__':
#     fname = 'access_log'        #access_log为apache日志文件
#     ip = '^(\d+\.){3}\d+'       # 1.11.123.45,  12345.11111.23423.2535234
#     br = 'Chrome|Firefox|MSIE'
#     print(count_patt(fname,ip))
#     print(count_patt(fname,br))

###分析apache访问日志--oop方式
#1统计每个客户访问apache服务器的次数
#2将统计信息通过字典方式显示出来
#3分别统计客户端是firefox和msie的访问次数
#4分别使用函数式编程和面向对象编程的方式实现
import re
class wenjianfenxi:                 #创建wenjianfenxi类
    def __init__(self,fname,patt):  #类中定义的函数叫做“方法”：
        #__init__ 为初始化实例属性
        self.name = fname
        self.patt = patt

    def count(self):        #间接调用被封装的内容
        #类中定义的函数叫做“方法”：count方法
        # print(self.name)
        # print(self.patt)
        patt_dict = {}
        cpatt = re.compile(self.patt)        #编译,self.patt = patt由参数传过来,ip或者br的正则
        with open(self.name) as fobj:       #打开文件，self.name = fname
            for line in fobj:           #遍历这个文件,获得每一行的内容
                m = cpatt.search(line)  #经过上面编译后,在这search每一行,返回符合ip正则或者br正则
                if m:                   # 如果匹配到内容，放到下面key变量，None表示False
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key,0) + 1
        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1.11.123.45,  12345.11111.23423.2535234
    br = 'Chrome|Firefox|MSIE'

    lb_ip = wenjianfenxi(fname,ip)
    print(lb_ip.count())
    # 根据wenjianfenxi类创建对象lb_ip对象，将fname,ip封装到lb_ip的fname 和 patt中

    lb_br = wenjianfenxi(fname,br)
    print(lb_br.count())
    # 根据wenjianfenxi类创建对象lb_br对象，将fname,br封装到lb_ip的fname 和 patt中










































