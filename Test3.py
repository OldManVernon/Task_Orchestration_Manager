import RPi.GPIO as GPIO
import time

LED_on = True
LED_off = False

currentLED = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    if GPIO.input(25) == 0:
        if currentLED == 1:
            GPIO.output(18, LED_on)
            GPIO.output(23, LED_off)
            GPIO.output(24, LED_off)
        if currentLED == 2:
            GPIO.output(18, LED_off)
            GPIO.output(23, LED_on)
            GPIO.output(24, LED_off)
        if currentLED == 3:
            GPIO.output(18, LED_off)
            GPIO.output(23, LED_off)
            GPIO.output(24, LED_on)
        if currentLED == 3:
            currentLED = 1
        else:
            currentLED += 1
        time.sleep(0.25)
