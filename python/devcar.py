import socket
import signal
import sys
from thread import *
import RPi.GPIO as GPIO

class DevBase:

	def __init__(self):
		pass

class DevGPIO(DevBase):
	def __init__(self):
		DevBase.__init__(self)
		
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		GPIO.setup(left, GPIO.OUT, GPIO.LOW)
		GPIO.setup(right, GPIO.OUT, GPIO.LOW)
		GPIO.setup(front, GPIO.OUT, GPIO.LOW)
		GPIO.setup(back, GPIO.OUT, GPIO.LOW)

		GPIO.output(left, GPIO.LOW)
		GPIO.output(right, GPIO.LOW)
		GPIO.output(front, GPIO.LOW)
		GPIO.output(back, GPIO.LOW)

	def decide(self, data):
		xDir, yDir = data.split(',')
		#~ if xDir ==  '1':
			#~ GPIO.output(left, GPIO.LOW)
			#~ GPIO.output(right, GPIO.HIGH)
		#~ elif xDir ==  '0':
			#~ GPIO.output(left, GPIO.LOW)
			#~ GPIO.output(right, GPIO.LOW)
		#~ elif xDir ==  '-1':
			#~ GPIO.output(left, GPIO.HIGH)
			#~ GPIO.output(right, GPIO.LOW)
			#~ 
		#~ if yDir ==  '1':
			#~ GPIO.output(back, GPIO.LOW)
			#~ GPIO.output(front, GPIO.HIGH)
		#~ elif yDir ==  '0':
			#~ GPIO.output(back, GPIO.LOW)
			#~ GPIO.output(front, GPIO.LOW)
		#~ elif yDir ==  '-1':
			#~ GPIO.output(back, GPIO.HIGH)
			#~ GPIO.output(front, GPIO.LOW)
		

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
		
				start_new_thread(self.clientthread, (conn,))
			
		except KeyboardInterrupt:
			self.kill_recived = True
		
		serverSocket.close()
		

	def clientthread(self, conn):
		control = DevGPIO
		conn.send('Welcomme to the server, type something')
		
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
