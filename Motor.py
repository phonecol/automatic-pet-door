import sys
import time
import RPi.GPIO as GPIO

mode = GPIO.getmode()

#GPIO.cleanup()

Forward = 26
Backward = 20
sleeptime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

def light_led(x):
	GPIO.output(19, GPIO.HIGH)
	time.sleep(x)
	GPIO.output(19, GPIO.LOW)

while(1):
    forward(5)
    light_led(5)
    reverse(5)

GPIO.cleanup()
