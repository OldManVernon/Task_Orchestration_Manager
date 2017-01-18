#RaspPiCode.py
#Should enable a 4 drive and 1 orientation motor robot with fixed IR sensors to detect and follow 90 degree turns

from __future__ import division
# imports the ability to do division
from time import sleep
# imported for the ability to suspend flow through code to enact motor control for fixed durations of time
import Adafruit_PCA9685
# imported the PCA9685 module for control of motors via Pi through Adafruit hat
import serial
# imported for the ability to read commuications coming from arduino uno
import time


# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

#set up the object for reading 
ser = serial.Serial('/dev/ttyACM0', 9600)
# ttyACMO is the usb serial port. this may change:
# type ls /dev/tty* with the cable plugged in
# type the same with the cable removed. the name thats gone
# is the name of the cable [likely ttyACM0 or ttyACM1]

time.sleep(2) #this is required since arduino resets upon
#establishment of connection. apparently.

def goSlow():
        pwm.set_pwm(0, 1024, 2048)
        pwm.set_pwm(1, 1024, 2048)
        pwm.set_pwm(2, 1024, 2048)
        pwm.set_pwm(3, 1024, 2048)

def goMed():
        pwm.set_pwm(0, 1024, 3072)
        pwm.set_pwm(1, 1024, 3072)
        pwm.set_pwm(2, 1024, 3072)
        pwm.set_pwm(3, 1024, 3072)

def TurnCC():
        pwm.set_pwm(4, 1024, 2048)
        sleep(1) #we're assuming it takes the motor 1 second at 25% speed to turn 270 degree left
        pwm.set_pwm(4, 0, 0)

def TurnC():
        pwm.set_pwm(4, 1024, 2048)
        sleep(0.3) #we're assuming it takes the motor 1 second at 25% speed to turn 270 degree left
        pwm.set_pwm(4, 0, 0)

#returns 1 for a left turn [via 270 clockwise]
#returns 0 for a 90 degree right turn
#the frame is stationary, what is turning is the direction that the four drive wheels point
def checkturn(str1, str2):
    indx = str1.index('1')
    if indx == -1:
        return -1
        #erroneous, there somehow wasn't a '1' in the nibble, we expect extacly one '1' in this nibble
    elif indx == 3: #it was the <bot> sensor check leading bit 
        return str2[0] == 1 #if the left sensor sees lines, we turn left, otherwise we return 0 for right turn
    else:
        return str2[indx+1] == 1 #clever way of checking the sensor to relative left now that we're sure to not index error

print 'Connection Up. Starting Loop.'
#ser.write('1') //this example only writes one byte
#initalize our not-quite-semaphores booleans
permission = True
#permission would be toggled if we had a killswitch implimented. 
expecting = False
executing = False
olddat = 0
pwm.set_pwm(0, 0, 0)
pwm.set_pwm(1, 0, 0)
pwm.set_pwm(2, 0, 0)
pwm.set_pwm(3, 0, 0)
pwm.set_pwm(4, 0, 0)
#make sure the robot is stationary by default

while permission :
    dat = int(ser.readline(), 2) #should read it as a base 2 num [binary]
    x = bin(dat).count("1")
    if (x == 1 and executing == False): #we are approaching a turn, slow down, 25% 
        goSlow()
        expecting = True
        olddat = dat #save what direction we were going to make sense of turn
    if (x ==2 and expecting):
        #we now see our turn
        turn = checkturn(olddat, dat)
        expecting = False
        executing = True
        if turn == 1:
            TurnCC()
        else:
            TurnC()
    if (x==2 and executing):
        goMed()
        sleep(1.5) #now safetly back on the tape
        executing = False
    print dat
    #used for debugging, only matters if Pi is connected via HDMI to a screen
    
#if we're out of the while loop the kill switch [not designed or coded] was hit, stop everything
pwm.set_pwm(0, 0, 0)
pwm.set_pwm(1, 0, 0)
pwm.set_pwm(2, 0, 0)
pwm.set_pwm(3, 0, 0)
pwm.set_pwm(4, 0, 0)
