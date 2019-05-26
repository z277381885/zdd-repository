import socket

host = ''            #表示0.0.0.0
port = 12345
addr = (host,port)

s = socket.socket()   #默认创建TCP套接字 s 为变量,可自定义
    #程序执行结束后,操作系统默认会保留套接字1分钟,在1分钟内无法再次使用相同的套接字 --如下取消
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)       #取消1分钟限制

s.bind(addr)                #绑定地址到套接字
s.listen(1)                 #启动监听过程   netstat -tlpn |grep :12345

while True:

    try:
        cli_sock , cli_addr = s.accept()    #接受客户端连接,收到连接返回(客户机套接字)并重新赋值给cli_sock , cli_addr
                                            #s.accept() 接受客户端连接,
    except KeyboardInterrupt:
        print(' 退出')
        break

    print('这个客户机连上来了: ',cli_addr)   #有client连上之后,在server端输出内容

    while True:
        data = cli_sock.recv(1024)      #等待接受客户端的数据.最多一次接收1024字节数据
        if data.strip() == b'quit':     #判断对方发送来的是否是quit,如果是则跳出循环,将关闭套接字
            break
        print(data.decode(),end='')     #server端输出客户端发送来的数据

        a = input('>:') + '\r\n'     #获取server端回复的信息
        # b = a.encode()          #将输入的字符转换为:bytes类型
        # cli_sock.send(b)        #向对方回复的数据必须是bytes类型,回复变量 b 的内容给对方
        cli_sock.send(a.encode()) #server端发送数据

    cli_sock.close()

s.close()
