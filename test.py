import RPi.GPIO as GPIO
import time

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)
while True:
    if GPIO.input(pin):
        print 'detected'
    else:
        print 'not detected'
    time.sleep(0.5)

'''
from gpiozero import MotionSensor
import time, random

pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("motion" + str(random.randint(1,100)))
        time.sleep(0.5)
'''
