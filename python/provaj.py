import RPi.GPIO as GPIO
import time

left = 7
right = 11
front = 13
back = 15

def init():
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

init()
GPIO.output(front, GPIO.HIGH)

time.sleep(2)
GPIO.output(front, GPIO.LOW)
GPIO.output(back, GPIO.HIGH)

time.sleep(2)


GPIO.cleanup()