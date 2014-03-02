#!/usr/bin/python

from flask import Flask, request
app = Flask(__name__)

import subprocess
sound_process = None

import ImgGet
img = None

@app.route("/")
def init():
    return "asciipe"

@app.route("/get/frame/")
def get_frame():
    if img == None:
        img = ImgGet.ImgGetter(13*5,8*5)
    print img.getImg()

@app.route("/get/user/")
def get_user():
    try:
        with open("user") as user_data:
            return user_data.read()
    except Error:
        return "Private Name"

@app.route("/get/sound/")
def start_sound():
    global sound_process
    if sound_process == None:
        sound_process = subprocess.Popen(['python','audio_client.py', request.remote_addr])
    return "Playing"

@app.route("/get/mute/")
def stop_sound():
    global sound_process
    sound_process.terminate()
    sound_process = None
    return "Muted"

if __name__ == "__main__":
    app.run('0.0.0.0', 8008)
