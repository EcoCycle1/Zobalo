from flask import Flask, render_template, jsonify
from time import sleep
#import time
import RPi.GPIO as GPIO
import random
from cumulocity_lib import create_measurement, create_event, create_alarm
from ultrasonic import plasticDist, userDist, binDist
from PACS import capture, classifier

from threading import Thread

# To run on other devices - flask run -h RPi IP Address
app = Flask(__name__) # Run as main app

# JSON DATA
# status: idle, home, count, reward
# can: Number of cans in current session
# plastic: Number of plastic bottles in current session
# load: Display loading gif when loading begins

# Cumolocity Template
# create_measurement("testMeasurement",25,"%") a- Name of Measurement, b- value, c-unit
# create_alarm("test_alarm","The can bin has overflown","MAJOR") a- Name of alarm, b- Message , c- Type of Alarm: WARNING, MINOR, MAJOR, CRITICAL 
# create_event("test_event", "Zobalo has restarted") a- Name of Event, b- Message

##### Initial States #####
plastic = 0
can = 0
status = 'idle'
canBin = 0
plasticBin = 0
z=0
canSum = 0
plasticSum = 0

tempo = random.randint(24,26)
create_measurement("intTemp", tempo, "C")

# Package Data into JSON Format for HTML Processing
@app.route('/data') 
def data(): 
    global plastic
    global can
    global status
    data = {"status": status, "num_can": can, "num_plas": plastic}
    return jsonify(data)

# Default Page Route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stop')
def stop():
    global status
    status = 'reward'
    return 'ok'

def mainFunc():
    global plastic
    global can
    global status

    while True:
        global plasticBin
        global canBin
        global detectBin
        global userDet
        global canSum
        global plasticSum

        z = 0

        detectBin = binDist()
        userDet = userDist()

        plasticBin = plasticDist()
        can = 0
        plastic = 0
        sleep(.1)
        if (canBin > 80):
            canBin = 5

        

        if ((detectBin <= 10) or (userDet <=45)):
            status = 'home'

            print('Home Page')
            while (status != 'reward'):
                j = 0
            #    y =  time.localtime()
             #   xs = int(time.strftime("%S", y))
              #  xm = int(time.strftime("%M", y))
               # xh = int(time.strftime("%H", y))
                #y = 60*xm+xs+xh*3600
                sleep(.2)
                #yx = y-x
                #if (yx>20 and status =='home'):
                 #   status = 'idle'
                  #  print('break')
                   # break

                if (binDist() <= 10):
                    status = 'count'
                    load = 1
                    capture()
                    img = classifier()
                    i=0
                    if (img == 'none'):
                        print('Did not identify')
                        

                    if (img == 'Plastic'):
                        plastic = plastic + 1
                        plasticSum = plasticSum + 1
                        t6=Thread(target=create_measurement,args=("plasticSum",plasticSum,"",))
                        t6.start()
                        z = 1
                        print('Detected Plastic')
                        plasticBin = plasticDist()
                        t3=Thread(target=create_measurement,args=("plasticLevel",plasticBin,"%",))
                        t3.start()
                        
                        

                    if (img == 'Can'):
                        can = can + 1
                        canSum = canSum + 1
                        t5=Thread(target=create_measurement,args=("canSum",canSum,"",))
                        t5.start()
                        print('Detcted Can')
                        z = 1
                        num1 = random.randint(0,3)
                        canBin = canBin + num1
                        t4=Thread(target=create_measurement,args=("canLevel",canBin,"%",))
                        t4.start()
                        

                        
        if (z == 1):
            sleep(15)
        if status != 'idle':
            status = 'idle'
            print("Idle Mode")

if __name__ == "__main__":
    t1 = Thread(target=mainFunc, args=())
    t1.daemon = True
    t1.start()
    app.run(host = '0.0.0.0', debug=False)
