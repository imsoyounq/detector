#!/bin/bash

#python /home/pi/detector/detector.py
#python /home/pi/detector/touch.py

export FLASK_APP=/home/pi/detector/app.py
flask run --host=0.0.0.0 --port=5000
