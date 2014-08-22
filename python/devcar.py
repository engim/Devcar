import socket
import signal
import sys
from thread import *
import RPi.GPIO as GPIO

class DevBase:

	def __init__(self):
		pass

class DevGPIO(DevBase):
	left = 7
	right = 11
	front = 13
	back = 15
	def __init__(self):
		DevBase.__init__(self)
		
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		GPIO.setup(self.left, GPIO.OUT, GPIO.LOW)
		GPIO.setup(self.right, GPIO.OUT, GPIO.LOW)
		GPIO.setup(self.front, GPIO.OUT, GPIO.LOW)
		GPIO.setup(self.back, GPIO.OUT, GPIO.LOW)

		GPIO.output(self.left, GPIO.LOW)
		GPIO.output(self.right, GPIO.LOW)
		GPIO.output(self.front, GPIO.LOW)
		GPIO.output(self.back, GPIO.LOW)

	def decide(self, data):
		if (data == ""):
			return
			
		xDir, yDir = data.split(',')
		xDir = float(xDir)
		yDir = float(yDir)
		
		
		if xDir == 1:
			print 'xDir: 1'
			GPIO.output(self.left, GPIO.LOW)
			GPIO.output(self.right, GPIO.HIGH)
		if xDir ==  0:
			print 'xDir: 0'
			GPIO.output(self.left, GPIO.LOW)
			GPIO.output(self.right, GPIO.LOW)
		if xDir ==  -1:
			print 'xDir: -1'
			GPIO.output(self.left, GPIO.HIGH)
			GPIO.output(self.right, GPIO.LOW)
		
		if yDir == 1:
			print 'yDir: 1'
			GPIO.output(self.back, GPIO.LOW)
			GPIO.output(self.front, GPIO.HIGH)
		if yDir ==  0:
			print 'yDir: 0'
			GPIO.output(self.back, GPIO.LOW)
			GPIO.output(self.front, GPIO.LOW)
			
		if yDir ==  -1:
			print 'yDir: -1'
			GPIO.output(self.back, GPIO.HIGH)
			GPIO.output(self.front, GPIO.LOW)

class DevConnection(DevBase):
	def __init__(self):
		DevBase.__init__(self)

class DevServer(DevConnection):
	
	def __init__(self, host='127.0.0.1', port = 44000):
		DevConnection.__init__(self)
		self.host = host
		self.port = port

	def create(self):
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.bind((self.host, self.port))
		
		serverSocket.listen(1)

		self.kill_recived = False
		
		try:
			while (1):
				(conn, addr) = serverSocket.accept()
				
				self.handleSocket(conn)
			
		except KeyboardInterrupt:
			self.kill_recived = True
		
		serverSocket.close()
		

	def handleSocket(self, conn):
		control = DevGPIO()
		conn.send('Welcomme to the server, type something')
		print 'New connection recived'
		while (not self.kill_recived):
			data = conn.recv(1024)
			if data == 'q':
				break
			else:
				try:
					control.decide(data)
				except:
					pass
		
		conn.close()

class DevMultiThreadServer(DevServer):
	def __init__(self, host='127.0.0.1', port = 44000):
		DevServer.__init__(self, host, port)

	def create(self):
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.bind((self.host, self.port))
		
		serverSocket.listen(1)

		self.kill_recived = False
		
		try:
			while (1):
				(conn, addr) = serverSocket.accept()
				
				start_new_thread(self.clientthread, (conn,))
			
		except KeyboardInterrupt:
			self.kill_recived = True
		
		serverSocket.close()
		

	def clientthread(self, conn):
		control = DevGPIO
		conn.send('Welcomme to the server, type something')
		print 'New connection recived'
		while (not self.kill_recived):
			data = conn.recv(1024)
			if data == 'q':
				break
			else:
				try:
					control.decide(data)
				except:
					pass
		
		conn.close()	





server = DevServer('192.168.1.31', 44000)
server.create()	
