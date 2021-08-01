import RPi.GPIO as GPIO
import time
servoy = 18
#servoPIN = 17
GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoy, GPIO.OUT)
GPIO.output(servoy, True)
#GPIO.output(servoPIN, True)

y = GPIO.PWM(servoy, 50) # GPIO 17 for PWM with 50Hz
#p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
time.sleep(0.5)
#p.start(5)
y.start(5)
time.sleep(0.5)
y.ChangeDutyCycle(2.5)
time.sleep(0.5)
