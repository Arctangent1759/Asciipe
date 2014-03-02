#################################################################
import socket
import pyaudio
import wave
import sys
from time import sleep
from threading import Thread

#record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40
PORT = 8009              # The same port as used by the server

class AudioProcess(Thread):
    def __init__(self):
        Thread.__init__(self)
        print "** Init **"
        self.host=False
        self.isRunning = False

    def run(self):
        print "** run **"
        while not self.host:
            sleep(.1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, PORT))
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        print("*recording")
        frames = []
        self.isRunning = True
        while self.isRunning:
            data  = stream.read(CHUNK)
            frames.append(data)
            s.sendall(data)
        print("*done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        s.close()

    def setHost(self,host):
        print "** SetHost {0} **".format(host)
        self.host=host

    def stop(self):
        print "** Stop **"
        self.isRunning=False
