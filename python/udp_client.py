import socket

host = '192.168.4.254'
port = 12345
addr = (host,port)

c = socket.socket(type=socket.SOCK_DGRAM)
while True:
    c.sendto(b'from client:nihao\r\n', addr)
    info = c.recvfrom(1024)
    print(info())

    if info.decode == 'quit':
        break
c.close()
