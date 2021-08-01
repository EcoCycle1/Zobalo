import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

ultTrig_plastic = 14
ultEcho_plastic = 15

ultTrig_user = 17
ultEcho_user = 21

ultTrig_detect = 10
ultEcho_detect = 9

GPIO.setup(ultTrig_plastic, GPIO.OUT)
GPIO.setup(ultEcho_plastic, GPIO.IN)

GPIO.setup(ultTrig_user, GPIO.OUT)
GPIO.setup(ultEcho_user, GPIO.IN)

GPIO.setup(ultTrig_detect, GPIO.OUT)
GPIO.setup(ultEcho_detect, GPIO.IN)

def plasticDist():
    GPIO.output(ultTrig_plastic, True)
    sleep(0.00001)
    GPIO.output(ultTrig_plastic, False)

    startTime = time.time()
    timeout = startTime + 0.04
    

    while GPIO.input(ultEcho_plastic) == 0 and startTime < timeout:
        startTime = time.time()

    stopTime = time.time()
    timeout = stopTime + 0.04

    while GPIO.input(ultEcho_plastic) == 1 and stopTime < timeout:
        stopTime = time.time()

    timeElp = stopTime - startTime
    plasticBin = (timeElp * 34300)/2


    plasticBin = plasticBin - 40
    plasticBin = (50 - plasticBin)*2


    #print("Plastic: ", int(plasticBin))

    return plasticBin

def userDist():
    GPIO.output(ultTrig_user, True)
    sleep(0.00001)
    GPIO.output(ultTrig_user, False)

    startTime3 = time.time()
    timeout3 = startTime3 + 0.04

    while GPIO.input(ultEcho_user) == 0 and startTime3 < timeout3:
        startTime3 = time.time()

    stopTime3 = time.time()
    timeout3 = stopTime3 + 0.04
    
    while GPIO.input(ultEcho_user) == 1 and stopTime3 < timeout3:
        stopTime3 = time.time()

    timeElp3 = stopTime3 - startTime3
    usrDet = (timeElp3 * 34300)/2

    #print("user: ",int(usrDet))

    return usrDet

def binDist():
    GPIO.output(ultTrig_detect, True)
    sleep(0.00001)
    GPIO.output(ultTrig_detect, False)

    startTime4 = time.time()
    timeout4 = startTime4 + 0.04
    

    while GPIO.input(ultEcho_detect) == 0 and startTime4 < timeout4:
        startTime4 = time.time()

    stopTime4 = time.time()
    timeout4 = stopTime4 + 0.04

    while GPIO.input(ultEcho_detect) == 1 and stopTime4 < timeout4:
        stopTime4 = time.time()

    timeElp4 = stopTime4 - startTime4
    garDet = (timeElp4 * 34300)/2

    #print("bin: ",int(garDet))

    return garDet
