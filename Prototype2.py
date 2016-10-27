import RPi.GPIO as GPIO
import time
def EngageEmergencyStop():
    # Once this routine is called, it will never return
    # since Emergency Stop means stop permanently
    # To continue, the program has to be stopped and restarted
    
    global EmergencyStopEngaged 

    global RotationMotor
    global DriveMotorRight
    global DriveMotorLeft

    global EmergencyStopSensor
    global PStartStopProgramSensor
    global MotorOn
    global MotorOff
    global ManueverTime

    global EmergencyStopEngaged
    EmergencyStopEngaged = True
    while EmergencyStopEngaged:
        GPIO.output(DriveMotorRight, MotorOff)
        GPIO.output(DriveMotorLeft, MotorOff)
        GPIO.output(RotationMotor, MotorOff) 
    # return is never reached
    return
def TurnWheels():
    # turn wheels assumes turn is one step
    # in all cases, EmergencyStop is checked
    
    global SensorOn
    global SensorOff
    
    global ProximitySensor1

    global DirectionSensor
    global LineSensorGroup1Right
    global LineSensorGroup1Center
    global LineSensorGroup1Left
    global LineSensorCenter

    global RotationMotor
    global DriveMotorRight
    global DriveMotorLeft

    global EmergencyStop
    global PStartStopProgram
    global MotorOn
    global MotorOff
    global ManueverTime
     
    Done = False;  
    Step = 1
    # could put in a time check as well to keep
    # robot from going in circles if there is a sensor failure
    while Done == False:
        if GPIO.input(EmergencyStopSensor, SensorOn):
            EngageEmergencyStop()
            # will never return
        else:
            if Step == 1:
                # need to move wheels enough to turn off the Direction Sensor
                # Step one turns on the left drive motor (to turn right) until the sensor goes off
                #    then it sets the Step to 1 to force next interation to the code that
                # watches for the Sensor to come back on
                if GPIO.input(DirectionSensor) == SensorOn:
                    GPIO.output(DriveMoRotationMotortorLeft, MotorOn) 
                else:
                    # go to next Step
                    Step = 2
            else: 
                #  keep turning until Direction Sensor is On
                if GPIO.input(DirectionSensor) == SensorOn: 
                    GPIO.output(RotationMotor, MotorOff)
                    Done = True
                else:
                    # continue turning
                    GPIO.output(RotationMotor, MotorOn) 
    return

def GoFoward(): 
 
    global SensorOn
    global SensorOff
    
    global ProximitySensor1

    global DirectionSensor
    global LineSensorGroup1Right
    global LineSensorGroup1Center
    global LineSensorGroup1Left
    global LineSensorCenter

    global RotationMotor
    global DriveMotorRight
    global DriveMotorLeft

    global EmergencyStop
    global PStartStopProgram
    global MotorOn
    global MotorOff
    global ManueverTime
    global DriveMotorRight
    global DriveMotorLeft

    global EmergencyStopSensor 
    global MotorOn
    global MotorOff
    global ManueverTime 
   
    global EmergencyStopEngaged
    global ManueverTicks
    
    global SensorOn
    global SensorOff
    
    Done = False
    StartTicks =  time.time()
    Step = 1
    while Done == False:
        if GPIO.input(EmergencyStopSensor, SensorOn):
            EngageEmergencyStop()
            # will never return
        if Step == 1: 
            EndTicks = time.time();
            TickDiff=EndTicks - StartTicks
            if TickDiff < ManueverTicks:
                GPIO.output(DriveMotorLeft, MotorOn)
                GPIO.output(DriveMotorRight, MotorOn)
                
            else:
                # stop moving
                GPIO.output(DriveMotorLeft, MotorOff)
                GPIO.output(DriveMotorRight, MotorOff)
                Done = True;
            # this is to handle if the obstacle is on a corner
            # and when going around it,it hits another line
            if GPIO.input(LineSensorCenter) == SensorOff:
                Step = 2
            else:
                # the sensor would normally be on
                # this verifies the robot has moved off the original line
                # nothing to do here
                Step = 3
        else:
            # sensor is now off
            # if it turns on, it has encountered a line
            if GPIO.input(LineSensorCenter) == SensorOn:
                GPIO.output(DriveMotorLeft, MotorOff)
                GPIO.output(DriveMotorRight, MotorOff)
                Done = True;
            else:
                EndTicks = time.time();
                TickDiff=EndTicks - StartTicks
                if TickDiff < ManueverTicks:
                    GPIO.output(DriveMotorLeft, MotorOn)
                    GPIO.output(DriveMotorRight, MotorOn)
                else: 
                    GPIO.output(DriveMotorLeft, MotorOff)
                    GPIO.output(DriveMotorRight, MotorOff)
                    Done = True; 
    return
def ManueverAround(): 

    global ProximitySensor1

    global DirectionSensor
    global LineSensorGroup1Right
    global LineSensorGroup1Center
    global LineSensorGroup1Left
    global LineSensorCenter

    global RotationMotor
    global DriveMotorRight
    global DriveMotorLeft

    global EmergencyStopSensor
    global StartStopProgramSensor
    global MotorOn
    global MotorOff
    global ManueverTime

    global SensorOn
    global SensorOff
    global EmergencyStopEngaged
    Done = False
    # logic
    # always go around object from the right
    # turn wheels right until DirectionSensor is off
    # continue wheels right until DirectionSensor sensor is on  
    # go forward manueverTime seconds
    # do the following 3 times
    #    rotate wheels to the right until DirectionSensor is off
    #    continue rotating wheels until direction sensor is on
    # this effectively moves the wheels back to original location
    
    # go forward for 2x base time OR until Line is encountered
    #   whichever one comes first.
    #   if Line is encountered,
    #     it means the line is going right
    #     need to go forward until robot is centered on line
    #     
    #     Rotate wheels to right until Direction Sensor is off
    #     continue rotating until direction sensor is on
    #     robot is now ready to continue normal proces
    #     return control
     
  
    if GPIO.input(EmergencyStopSensor, SensorOn):
        EngageEmergencyStop()
        # will never return
            
    TurnWheels() # 90 degrees 

    GoForward()
    
    if GPIO.input(LineSensorGroup1Center) == SensorOff:
        TurnWheels()
        TurnWheels()
        TurnWheels()
        GoForward()
    else:
        TurnWheels()
        return
            

    # if no line encountered, try one more time to go forward
    if GPIO.input(LineSensorGroup1Center) == SensorOff:
        GoForward()
    else: # line found, turn right
        TurnWheels()        
        return
    
        
    if GPIO.input(LineSensorGroup1Center) == SensorOff:     
        TurnWheels()
        TurnWheels()
        TurnWheels()
        GoForward()
        
    # if line not found, go forward
    if GPIO.input(LineSensorGroup1Center) == SensorOff:
        GoForward()  
    else:
        TurnWheels()
        return

     # if line not found, go one more time
    if GPIO.input(LineSensorGroup1Center) == SensorOff: 
        GoForward()
    else: 
        return

    # if line not found, rotate 270 degrees 
    EngageEmergencyStop();
    return

GPIO4 = 4   # pin 7 usable .
GPIO17 = 17 # pin 11 usable.
GPIO27 = 27 # pin 13 usable.
GPIO22 = 22 # pin 15 usable.
GPIO5 = 5   # pin 29 usable.
GPIO6 = 6   # pin 31 usable.
GPIO13 = 13 # pin 33 usable.
GPIO26 = 26 # pin 37 usable
GPIO23 = 23 # pin 16 usable
GPIO24 = 24 # pin 18 usable.
GPIO25 = 25 # pin 22 usable.
GPIO12=12   # pin 32 usable
GPIO16 = 16 # pin 36 usable.
PCM_DIN = 20 #GPIO 20 pin 38
PCM_DOUT = 21  #GPIO 21 pin 40
PCM_FS = 19 # GPIO 19 pin 35
SPI_CE0 = 8  # GPIO 8 pin 24
SPI_CEO = 7   # GPIO 7 pin 26
SPI_MOSI = 10 # GPIO 10 pin 19
SPI_MISO = 9 # GPIO 9 pin 21
SPI_SCLK = 11 # GPIO 11`pin 23
PCM_CLK = 18 # GPIO 18 pin 18
UART_TXD = 14 # GPIO 14 pin 8
UART_RXD = 15 # GPIO15  pin 10

ProximitySensor1 = GPIO4

LineSensorGroup1Right = GPIO17  # located on arm
LineSensorGroup1Center = GPIO27 # located on arm
LineSensorGroup1Left = GPIO22   #  located on arm
 
 
DirectionSensor=GPIO13
RotationMotor = GPIO23
DriveMotorRight = GPIO24
DriveMotorLeft = GPIO25

EmergencyStopSensor = GPIO5
StartProgramSensor = GPIO6

EmergencyStopEngaged=False

SensorOn=True
SensorOff=False

Done = False
MotorOn = True
MotorOff = False
ManueverTicks=5 # check to see if it is seconds or milliseconds

dmy=0;
# Main Driver Loop

GPIO.setmode(GPIO.BCM)
GPIO.setup(ProximitySensor1,GPIO.IN) 
GPIO.setup(LineSensorGroup1Right,GPIO.IN)
GPIO.setup(LineSensorGroup1Left,GPIO.IN)
GPIO.setup(DirectionSensor,GPIO.IN)
GPIO.setup(RotationMotor,GPIO.OUT)
GPIO.setup(DriveMotorRight,GPIO.OUT)
GPIO.setup(DriveMotorLeft,GPIO.OUT)
GPIO.setup(EmergencyStopSensor,GPIO.IN)
GPIO.setup(StartProgramSensor,GPIO.IN)
GPIO.setup(ProximitySensor1,GPIO.IN)
GPIO.setup(ProximitySensor1,GPIO.IN)
GPIO.setup(ProximitySensor1,GPIO.IN)
GPIO.setwarnings(False) 

while Done == False:
    if GPIO.input(StartProgramSensor) == SensorOff:
        GPIO.output(RotationMotor, MotorOff)
        GPIO.output(DriveMotorRight, MotorOff)
        GPIO.output(DriveMotorLeft, MotorOff)
    else:
        if GPIO.input(EmergencyStopSensor, SensorOn):
            # will never return
            # but just in case
            Done = True
            EngageEmergencyStop()  
        else:
            if GPIO.input(StartProgramSensor) == SensorOn:
                # check Proximity Sensor for barrier
                if GPIO.input(ProximitySensor1) == SensorOn :
                    # manuever around routine
                    # this will go around and realign to contine
                    # stop moving forward
                    GPIO.output(DriveMotorLeft, MotorOff)
                    GPIO.output(DriveMotorRight, MotorOff)
                    ManueverAround()
                    #  robot always turns right
                    #  turn wheels 90 degrees
                    #  if next line found, continue progress
                    #  if next line not found, it means the direction is the other way
                    #  this means turning wheels another 180 degrees : turn wheels twice             
                else:
                    if GPIO.input(LineSensorGroup1_Center) == SensorOn:
                        # check if either right or left sensor is on
                        # whichever one is on, one side of the motor bank
                        # needs to be shut off
                        if GPIO.input(LineSensorGroup1_Right) == SensorOff:
                            if GPIO.input(LineSensorGroup1_Left) == SensorOff:
                                # both sensors are off the tape
                                # need to turn stop
                                GPIO.output(DriveMotorLeft, MotorOff)
                                GPIO.output(DriveMotorRight, MotorOff)
                                # now turn 90 degrees
                                TurnWheels()
                                # if the center sensor is on, it means the path is the other direction
                                # rotate two more times
                                if GPIO.input(LineSensorGroup1_Center) == SensorOn: 
                                    TurnWheels()
                                    TurnWheels() 
                                    # now it should be ready
                                else:
                                    # it should be ready to go
                                    # could put code here to verify at least one front sensor if on
                                    # if none are on, robot is lost
                                    # for now, let the next cycle check this.
                                    dmy=0
                            else: 
                                # this means the left is on and right is off
                                # need to turn left
                                # turn on right motor
                                # turn off left motor 
                                GPIO.output(DriveMotorLeft, MotorOff)
                                GPIO.output(DriveMotorRight, MotorOn) 
                        else: # Right is on, so check Left
                            if GPIO.input(LineSensorGroup1_Left) == SensorOff: 
                                GPIO.output(DriveMotorLeft, MotorOn)
                                GPIO.output(DriveMotorRight, MotorOff)
                            else:
                                # Both are on. go straight
                                GPIO.output(DriveMotorLeft, MotorOn)
                                GPIO.output(DriveMotorRight, MotorOn) 
                    else: # this means LineSensorGroup1_Center is not on
                        # this can occur on a turn, so go forward
                        # logic can be added to make sure at least one front sensor is active
                        # if all three are off at this point, robot is lost
                        # need to stop
                    
                        if GPIO.input(LineSensorGroup1_Right) == SensorOff:  
                             if GPIO.input(LineSensorGroup1_Left) == SensorOff:
                                 # all three sensors are off, meaning the robot is lost
                                 Done = True
                                 EngageEmergencyStop()
                                 # will never come through
                             else:
                                # turn on Left motor, Right motor off  
                                GPIO.output(DriveMotorLeft, MotorOn) 
                                GPIO.output(DriveMotorRight, MotorOff)
                        else: # this means right is on. now check left
                            if GPIO.input(LineSensorGroup1_Left) == SensorOff:  
                                GPIO.output(DriveMotorLeft, MotorOn) 
                                GPIO.output(DriveMotorRight, MotorOff)
                            else: # turn both on
                                GPIO.output(DriveMotorLeft, MotorOn) 
                                GPIO.output(DriveMotorRight, MotorOn)
            else: # Program switch has not been turned on. turn off motors
                GPIO.output(DriveMotorLeft, MotorOff) 
                GPIO.output(DriveMotorRight, MotorOff ) 


