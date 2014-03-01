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

if __name__ == "__main__":
    app.run('0.0.0.0', 8008)
