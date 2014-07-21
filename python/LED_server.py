import socket   #for sockets
import signal	# for signal (oh, what a surprise!)
import sys
from thread import *
import RPi.GPIO as GPIO



# Defining constants
left = 7
right = 11
front = 13
back = 15

def initGPIO():
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


def switchData(data):
	xDir, yDir = data.split(',')
	if xDir ==  '1':
		GPIO.output(left, GPIO.LOW)
		GPIO.output(right, GPIO.HIGH)
	elif xDir ==  '0':
		GPIO.output(left, GPIO.LOW)
		GPIO.output(right, GPIO.LOW)
	elif xDir ==  '-1':
		GPIO.output(left, GPIO.HIGH)
		GPIO.output(right, GPIO.LOW)
		
	if yDir ==  '1':
		GPIO.output(back, GPIO.LOW)
		GPIO.output(front, GPIO.HIGH)
	elif yDir ==  '0':
		GPIO.output(back, GPIO.LOW)
		GPIO.output(front, GPIO.LOW)
	elif yDir ==  '-1':
		GPIO.output(back, GPIO.HIGH)
		GPIO.output(front, GPIO.LOW)
	
	
	
def clientthread(conn):
	conn.send('Welcomme to the server, type something')

	while (not kill_recived):
		data = conn.recv(1024)
		if data == 'q':
			break
		else:
			try:
				switchData(data)
			except:
				pass
	
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

initGPIO()
kill_recived = False
createServer()
GPIO.cleanup()

