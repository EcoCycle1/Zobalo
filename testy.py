from time import sleep
import RPi.GPIO as GPIO
import random
from cumulocity_lib import create_measurement, create_event, create_alarm
from ultrasonic import plasticDist, userDist, binDist
from PACS import capture, classifier

GPIO.setmode(GPIO.BCM) # Set GPIO to BCM Mode


##### Initial States #####
plastic = 0
can = 0
status = 'idle'
canBin = 0
plasticBin = 0
z=0

def mainFunc():
    global plastic
    global can
    global status

    while True:
        global plasticBin
        global canBin
        global detectBin
        global userDet

        z = 0

        detectBin = binDist()
        userDet = userDist()

        plasticBin = plasticDist()
        can = 0
        plastic = 0
        sleep(1)
        if (canBin > 80):
            canBin = 5

        if ((detectBin <= 13) or (userDet <=60)):
            status = 'home'
            print('Home Page')
            while (status != 'reward'):
                j = 0
                sleep(1)
                if (binDist() <= 13):
                    status = 'count'
                    capture()
                    img = classifier()
                    i=0
                    while (img == 'none'):
                        print('Did not identify')
                        capture()
                        img = classifier()
                        i = i + 1
                        if (i > 5):
                            j = 1
                            break
                    if (j==1):
                        continue

                    if (img == 'Plastic'):
                        plastic = plastic + 1
                        z = 0
                        print('Detected Plastic')

                    if (img == 'Can'):
                        can = can + 1
                        print('Detcted Can')
                        z = 1
                        num1 = random.randint(3,8)
                        canBin = canBin + num1
                        create_measurement("c8y_fillLevel",canBin,"%")
                    
                    plasticBin = plasticDist()
                    create_measurement("testMeasurement",plasticBin,"%")
                    
            
    if (z == 1):
        sleep(15)
    status = 'idle'
    print("Idle Mode")

mainFunc()