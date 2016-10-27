import RPi.GPIO as GPIO
import time

LED_on = True
LED_off = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)
while True:
    if GPIO.input(25):
       GPIO.output(18, LED_off)
    else:
       GPIO.output(18, LED_on) 
