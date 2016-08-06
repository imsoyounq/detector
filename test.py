import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 3
GPIO.setup(pin, GPIO.IN)


alreadyPressed = False

while True:
    pressed = GPIO.input(pin)

    if pressed and not alreadyPressed:
        print 'pressed'

    alreadyPressed = pressed
    time.sleep(1)
