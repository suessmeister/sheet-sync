# Trying to use as little libraries as possible to complete the project! Need to beat the Python Developer Stereotype....

# Absolutely required libraries. In other words, WE NEED THESE!
import pyaudio  # allows us to work with audio in python and will be for recording
import aubio
import numpy as np

# Libraries that are still undecided.
from tkinter import *

# Libraries just for fun, either for testing purposes or else.


FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100  # represents the hertz value
FRAMES_PER_BUFFER = 1024

WINDOW_SIZE = 4096
HOP_SIZE = FRAMES_PER_BUFFER


audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    rate=RATE,
    channels=CHANNELS,
    frames_per_buffer=FRAMES_PER_BUFFER,
    input=True,
)  # frames per buffer is the chunk size


pitcher = aubio.pitch(
    "default", WINDOW_SIZE, HOP_SIZE, RATE
)  # create aubio pitch detection
pitcher.set_unit("Hz")  # set output unit, can be midi, cent, Hz
pitcher.set_silence(-25)  # ignore frames under this level, in db

print("listening...")


while True:
    try:
        data = stream.read(FRAMES_PER_BUFFER)
        samples = np.frombuffer(data, dtype=np.float32)
        pitch = pitcher(samples)[0]
        if pitch > 0.0:
            print(pitch)
    except KeyboardInterrupt:
        print("ctrl-c pressed. stopping... ")
        break
    except IOError as e:
        print(f"error reading from stream: {e}")
        break

print("quitting...")
stream.stop_stream()
stream.close()
audio.terminate()
