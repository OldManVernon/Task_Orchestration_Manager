import RPi.GPIO as GPIO
import time

LED_on = True
LED_off = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, LED_on)
GPIO.output(18, LED_off)
