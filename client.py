#!/usr/bin/python
from flask import Flask, request
import ImgGet
import audio_client

app = Flask(__name__)

img_obj = ImgGet.ImgGetter(120,40)
audio_obj = audio_client.AudioProcess()
audio_obj.start()

@app.route("/")
def init():
    print "asciipe"
    return "asciipe"

@app.route("/get/frame/")
def get_frame():
    print "getframe"
    return img_obj.getImg()

@app.route("/get/user/")
def get_user():
    print "Private Name"
    try:
        with open("user") as user_data:
            return user_data.read()
    except Error:
        return "Private Name"

@app.route("/get/sound/")
def start_sound():
    print "Playing"
    audio_obj.setHost(request.remote_addr)
    print "foobar"
    return "Playing"

@app.route("/get/mute/")
def stop_sound():
    print "Muted"
    audio_obj.stop()
    return "Muted"

if __name__ == "__main__":
    app.run('0.0.0.0', 8008)
