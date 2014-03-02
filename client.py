#!/usr/bin/python
from flask import Flask, request
import subprocess
import ImgGet
import audio_client

app = Flask(__name__)

img_obj = ImgGet.ImgGetter(120,40)
audio_obj = audio_client.AudioProcess()

@app.route("/")
def init():
    return "asciipe"

@app.route("/get/frame/")
def get_frame():
    return img_obj.getImg()

@app.route("/get/user/")
def get_user():
    try:
        with open("user") as user_data:
            return user_data.read()
    except Error:
        return "Private Name"

@app.route("/get/sound/")
def start_sound():
    sound_obj.setHost(request.remote_addr)
    return "Playing"

@app.route("/get/mute/")
def stop_sound():
    sound_process.stop()
    return "Muted"

if __name__ == "__main__":
    app.run('0.0.0.0', 8008)
