import socket   #for sockets
import signal	# for signal (oh, what a surprise!)
import sys
from thread import *



def clientthread(conn):
	conn.send('Welcomme to the server, type something')

	while (not kill_recived):
		data = conn.recv(1024)
		print data
		if not data:
			break
	
	conn.close()

def createServer():
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind(('192.168.1.131', 44000))

	print 'Socket created'

	serverSocket.listen(5)


	try:
		while (1):
			(conn, addr) = serverSocket.accept()
			print 'connection recived'
	
			start_new_thread(clientthread, (conn,))
		
	except KeyboardInterrupt:
		kill_recived = True

	


	serverSocket.close()

kill_recived = False
createServer()

