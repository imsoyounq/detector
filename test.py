import RPi.GPIO as GPIO
import time
import random

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)
state = False
while True:
    new_state = GPIO.input(pin)
    if new_state != state:
        if new_state:
            print 'detected'
        else:
            print 'not detected'
        state = new_state
        print str(time.time())

'''
from gpiozero import MotionSensor
import time, random

pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("motion" + str(random.randint(1,100)))
        time.sleep(0.5)
'''
