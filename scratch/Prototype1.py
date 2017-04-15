import RPi.GPIO as GPIO
import time
def GoForward():
    
    LED_on = True
    LED_off = False
    Done = False
    currentLED = 0 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.IN)
    while Done == False:
        if GPIO.input(25) == 0:
            if currentLED == 0: 
                GPIO.output(18, LED_off)
                GPIO.output(23, LED_off)
                GPIO.output(24, LED_off) 
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
            if currentLED == 4:
                Done = True 
                GPIO.output(18, LED_off)
                GPIO.output(23, LED_off)
                GPIO.output(24, LED_off) 
            else:
                currentLED += 1
            time.sleep(0.25)
    return
Done = False;

GPIO4 = 4   # pin 7 usable
GPIO17 = 17 # pin 11 usable
GPIO27 = 27 # pin 13 usable
GPIO22 = 22 # pin 15 usable
GPIO5 = 5   # pin 29 usable
GPIO6 = 6   # pin 31 usable
GPIO13 = 13 # pin 33 usable
GPIO26 = 26 # pin 37 usable
GPIO23 = 23 # pin 16 usable
GPIO24 = 24 # pin 18 usable
GPIO25 = 25 # pin 22 usable
GPIO12=12   # pin 32 usable
GPIO16 = 16 # pin 36 usable
PCM_DIN = 20 #GPIO 20 pin 38
PCM_DOUT = 21  #GPIO 21 pin 40
PCM_FS = 19 # GPIO 19 pin 35
SPI_CE0 = 8  # GPIO 8 pin 24
SPI_CEO = 7   # GPIO 7 pin 26
SPI_MOSI = 10 # GPIO 10 pin 19
SPI_MISO = 21 # GPIO 9 pin 21
SPI_SCLK = 23 # GPIO 11`pin 23
PCM_CLK = 18 # GPIO 18 pin 18
UART_TXD = 14 # GPIO 14 pin 8
UART_RXD = 15 # GPIO15  pin 10

Proximity_Sensor1 = GPIO4

LineSensorGroup1_Right = GPIO17
LineSensorGroup1_Center = GPIO27
LineSensorGroup1_Left = GPIO22

LineSensorGroup2_Right = GPIO17
LineSensorGroup2_Center = GPIO27
LineSensorGroup2_Left = GPIO22

#LineSensorGroup3_Right = GPIO17
#LineSensorGroup3_Center = GPIO27
#LineSensorGroup3_Left = GPIO22

#LineSensorGroup4_Right = GPIO17
#LineSensorGroup4_Center = GPIO27
#LineSensorGroup4_Left = GPIO22

RotationSensor1 = GPIO23
RotationSensor2 = GPIO23
RotationSensor3 = GPIO23
RotationSensor4 = GPIO23

RotationMotor = GPI024;
DriveMotor = GPIO25;

While Done == False:
    GoForward()


