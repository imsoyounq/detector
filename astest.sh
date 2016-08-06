#!/bin/bash

python /home/pi/detector/detector.py

export FLASK_APP=app.py
flask run
