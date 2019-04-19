import socket

server = '192.168.4.254'    #服务端地址
port = 12345                #服务端TCP服务器端口
addr = (server,port)
c = socket.socket()           #创建套接字
c.connect(addr)             #连接服务端

while True:
    data = input('quit to end >') + '\r\n'  #上面服务端程序做的是先收再发,这边客户端就先发再收
    c.send(data.encode())                   #将输入的数据转换成bytes类型,发送给服务端
    if data.split() == 'quit':              #将输入的字符串去掉两边空白(split的作用),再判断
        break
    rdata = c.recv(1024)                    #接受对方(服务端)的数据
    print(rdata.decode(),end='')
c.close()
