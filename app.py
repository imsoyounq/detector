import os, subprocess, shlex, sys
from flask import Flask, render_template, redirect, url_for, flash, session, request

app = Flask(__name__)

@app.route("/")
def undetecting():    
   return render_template('undetecting.html') 

@app.route("/detecting")
def detect_on():
    subprocess.Popen(shlex.split('python detector.py'))
    return render_template('detecting.html')

@app.route("/undetecting")
def detect_off():
    subprocess.Popen(shlex.split('pkill omxplayer'))
    return redirect(url_for('undetecting'))

@app.route("/shutdown")
def shutdown():
    subprocess.Popen(shlex.split('sudo shutdown now'))
    data = {''}
    return redirect(url_for('undetecting'), data=data)

@app.route("/help")
def help():
    return render_template('help.html')

@app.errorhandler(404)
def error():
    return redirect(url_for('help')) 


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)
