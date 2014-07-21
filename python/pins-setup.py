#test de funcionament i numeracio del pins del sostre del cotxe (una mena de Hello World)

import RPi.GPIO as GPIO
import time

FRONT =	13
BACK =	15
LEFT =	7
RIGHT =	11

def setupPins():
	# to use Raspberry Pi board pin numbers
	GPIO.setmode(GPIO.BOARD)

	# set up GPIO output channel
	GPIO.setup(FRONT, GPIO.OUT)
	GPIO.setup(BACK, GPIO.OUT)
	GPIO.setup(LEFT, GPIO.OUT)
	GPIO.setup(RIGHT, GPIO.OUT)
	# set RPi board pin 12 low
	GPIO.output(FRONT, GPIO.LOW)
	GPIO.output(BACK, GPIO.LOW)
	GPIO.output(LEFT, GPIO.LOW)
	GPIO.output(RIGHT, GPIO.LOW)

setupPins()

you_mad = 0
while you_mad != 1:
	# set RPi board pin 12 high
	GPIO.output(FRONT, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(BACK, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(LEFT, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(RIGHT, GPIO.HIGH)

	time.sleep(0.2)

	# set RPi board pin 12 low
	GPIO.output(FRONT, GPIO.LOW)
	GPIO.output(BACK, GPIO.LOW)
	GPIO.output(LEFT, GPIO.LOW)
	GPIO.output(RIGHT, GPIO.LOW)
	
	time.sleep(0.2)

# to reset every channel that has been set up by this program to INPUT with no pullup/pulldown and no event detection.
GPIO.cleanup()
