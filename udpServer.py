#UDP Server

from socket import *
from time import ctime
HOST = ''
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST,PORT)
uServSock = socket(AF_INET,SOCK_DGRAM)
uServSock.bind(SOCKADDR)
while True:
	print ('waiting:')
	data,addr = uServSock.recvfrom(BUFSIZE)
	loc_data = data.decode('utf-8') 
	print ('receivedd from: ', addr, ' data: ', loc_data )
	uServSock.sendto(bytearray('[%s] %s' % (ctime(),data), encoding="utf-8"), addr)
uServSock.close()
