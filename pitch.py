import pyaudio  # allows us to work with audio in python and will be for recording
import keyboard
import aubio
import numpy as np


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
pitcher.set_silence(-20)  # ignore frames under this level, iqn db
print("listening...")

try:
    while True:
        data = stream.read(FRAMES_PER_BUFFER)
        samples = np.frombuffer(data, dtype=np.float32)
        freq = pitcher(samples)[0]
        if freq > 0.0:
            print(freq)
        if keyboard.is_pressed("space"):
            print("quitting...")
            break


finally:
    stream.stop_stream()
    audio.terminate()
    stream.close()
