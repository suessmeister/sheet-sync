import pyaudio  # allows us to work with audio in python and will be for recording
import keyboard
import aubio


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # represents the hertz value
FRAMES_PER_BUFFER = 1024

WINDOW_SIZE = 4096
HOP_SIZE = WINDOW_SIZE // 2

audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    rate=RATE,
    channels=CHANNELS,
    frames_per_buffer=FRAMES_PER_BUFFER,
    input=True,
)  # frames per buffer is the chunk size


pitcher = aubio.pitch("default", WINDOW_SIZE, HOP_SIZE, RATE)

print("test")
try:
    while True:
        data = stream.read(1024)
        if keyboard.is_pressed("q"):
            print("quitting...")
            break


finally:
    stream.stop_stream()
    audio.terminate()
    stream.close()
