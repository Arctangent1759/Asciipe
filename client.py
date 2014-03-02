#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def init():
    return "asciipe"

@app.route("/get/frame/")
def get_frame():
    return "FRAME as ASCII"

@app.route("/get/user/")
def get_user():
    try:
        with open("user") as user_data:
            return user_data.read()
    except Error:
        return "Private Name"

@app.route("/post/sound/", methods=['GET', 'POST'])
def post_sound(sound_data):
    app.logger.info('Info')

if __name__ == "__main__":
    app.run('0.0.0.0', 8008)
