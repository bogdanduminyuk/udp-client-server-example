#UDP Client
from socket import *
HOST = '192.168.1.2'
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST,PORT)
uCliSock = socket(AF_INET,SOCK_DGRAM)
while True:
        data = input('>')
        print (data)
        data = bytearray(data, encoding='utf-8')
        if not data: break
        uCliSock.sendto(data, SOCKADDR)
        data, addr = uCliSock.recvfrom(BUFSIZE)
        if not data: break
uCliSock.close()
