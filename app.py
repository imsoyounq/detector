import os, subprocess, shlex, sys, random
from flask import Flask, render_template, redirect, url_for, flash, session, request
import RPi.GPIO as GPIO
import time
from multiprocessing import Process

app = Flask(__name__)
detector_on = False


@app.route("/")
def undetecting():    
    return render_template('undetecting.html') 

@app.route("/detecting")
def detect_on():
    global detector_on
    if not detector_on:
        detector_on = True
    return render_template('detecting.html') 

@app.route("/undetecting")
def detect_off():
    subprocess.Popen(shlex.split('pkill omxplayer'))
    global detector_on
    detector_on = False
    return redirect(url_for('undetecting'))

def rndmplay():
    randomfile = random.choice(os.listdir("/home/pi/wakeup/"))
    os.system('omxplayer /home/pi/wakeup/' + randomfile)

@app.route("/shutdown")
def shutdown():
    subprocess.Popen(shlex.split('sudo shutdown now'))
    data = {''}
    return

@app.route("/help")
def help():
    return render_template('help.html')

@app.errorhandler(404)
def error():
    return redirect(url_for('help')) 


def motion_detect():

    rndmplay()


def touch(): 
    global mdp, touch_pin, motion_on, pressed, alreadyPressed

    while True:
        pressed = GPIO.input(touch_pin)
        if pressed and not alreadyPressed:
            print 'pressed'
            if motion_on:
                motion_on = False
                if mdp is not None:
                    mdp.terminate()
                    mdp = None
            else:
                motion_on = True
                mdp = Process(target=motion_detect)
                mdp.start()

        alreadyPressed = pressed
        time.sleep(0.1)


mdp = None
motion_on = False
touch_pin = 3
motion_pin = 4
pressed = False
alreadyPressed = False

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch_pin, GPIO.IN)
    GPIO.setup(motion_pin, GPIO.IN)
    p = Process(target=touch)
    p.start()

    app.run(host = '0.0.0.0', port=5000)
