import pyaudio
import wave
import urllib
import urllib2

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

url = 'http://127.0.0.1:8008/post/sound/'
data = urllib.urlencode({'FORMAT' : format,
                         'CHANNELS'  : CHANNELS,
                         'RATE' : RATE})
response = urllib2.urlopen(url=url, data= b''.join(frames)).read()
assert(response == "Successfully Played")
