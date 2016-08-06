import time, random, os 
import RPi.GPIO as gpio
import shlex, subprocess
gpio.setmode(gpio.BCM)
 
'''
pir_pin = 4
 
gpio.setup(pir_pin, gpio.IN)         # activate input
 
while True:
    if gpio.input(pir_pin):
        print("motion" + str(random.randint(1,100)))
    time.sleep(0.1)
'''
def rndmplay():
    randomfile = random.choice(os.listdir("/home/pi/wakeup/"))
    file = '/home/pi/wakeup/' + randomfile
    os.system('omxplayer ' + file)

while True:
    print "ALARM ON"
    rndmplay()
    if KeyboardInterrupt:
        print "ALARM OFF"
        break
#subprocess.Popen(shlex.split('q'))

