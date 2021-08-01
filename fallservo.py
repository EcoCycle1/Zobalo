import RPi.GPIO as GPIO
import time

servoy = 18
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoy, GPIO.OUT)

y = GPIO.PWM(servoy, 50) # GPIO 17 for PWM with 50Hz
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

def drop():
    time.sleep(0.5)
    p.start(5)
    y.start(7.5)
    time.sleep(0.5)
    p.stop()
    y.stop()

def rest():
    time.sleep(0.5)
    p.start(7.8) # Initialization
    y.start(4.7)
    time.sleep(0.5)
    p.stop()
    y.stop()

drop()

GPIO.cleanup()