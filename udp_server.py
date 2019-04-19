import  socket

port = 12345
host = ''
addr = (host,port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

while True:
    data , cli_addr = s.recvfrom(1024)  #一次最多接收1024字节数据，返回值是(数据，客户机地址)
    print(data.decode(),end='')
    
    a = input('server>')
    s.sendto(a.encode()  , cli_addr)  #项客户端地址发送数据
    if a.strip() == 'quit':
        break
s.close()
