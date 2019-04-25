# import paramiko
# import sys
# import getpass
# import os
# import threading
#
# def rcmd(host, user='root', passwd=None, port=22, cmd=None):
#     ssh = paramiko.SSHClient()                                 #创建连接
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #相当于在连接是输入yes
#     ssh.connect(host, username=user, password=passwd, port=port)  #连接
#     stdin, stdout, stderr = ssh.exec_command(cmd)   #命令结果为一个元组,有三个元素,分别赋值
#     out = stdout.read()             #得到的是bills类型数据,需要out.decode()转成字符
#     error = stderr.read()
#     if out:                         #如果输出不为空,有输出
#         print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
#     if error:                       #如果错误不为空,有错误
#         print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, error.decode()))
#     ssh.close()                     #关闭连接
#
# if __name__ == '__main__':
#     if len(sys.argv) != 3:          #判断是不是三个参数都有
#         print("Usage: %s ipfile 'command'" % sys.argv[0])
#         exit(1)
#
#     ipfile = sys.argv[1]                    #第2个位置参数,第1个默认为本身python文件本身
#     if not os.path.isfile(ipfile):          #如果主机地址文件没有
#         print('No such file:', ipfile)
#         exit(2)
#
#     passwd = getpass.getpass()          #输入密码,密文方式
#
#     command = sys.argv[2]               #第3个位置参数
#
#     with open(ipfile) as fobj:
#         for line in fobj:
#             ip = line.strip()
#             # rcmd(ip, passwd=passwd, cmd=command)  改用多线程
#             t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': passwd, 'cmd': command})
#             t.start()
#             # 拆分多线程命令:target(*args, **kwargs)
#             # 拆分多线程传参:target(ip, passwd=passwd, cmd=command)
#
# ##  ]# python3 paramikotest.py paramikoip.txt 'sleep 3 ;id root'
# # 执行命令时,多个参数用单引号,用;号隔开
#






















