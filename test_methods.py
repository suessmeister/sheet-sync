import pyaudio
import sys
import aubio
import numpy as np


def test_input_devices():
    audio = pyaudio.PyAudio()
    for i in range(audio.get_device_count()):
        device = audio.get_device_info_by_index(i)
        print(f"Device {i}: {device['name']}")


def frequency_demo_aubio():
    # initialise pyaudio
    p = pyaudio.PyAudio()

    # open stream
    buffer_size = 1024
    pyaudio_format = pyaudio.paFloat32
    n_channels = 1
    samplerate = 44100
    stream = p.open(
        format=pyaudio_format,
        channels=n_channels,
        rate=samplerate,
        input=True,
        frames_per_buffer=buffer_size,
    )

    # if len(sys.argv) > 1:
    #     # record 5 seconds
    #     output_filename = sys.argv[1]
    #     record_duration = 5  # exit 1
    #     outputsink = aubio.sink(sys.argv[1], samplerate)
    #     total_frames = 0
    # else:
    #     # run forever
    #     outputsink = None
    #     record_duration = None

    # setup pitch
    tolerance = 0.8
    win_s = 4096  # fft size
    hop_s = buffer_size  # hop size
    pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
    pitch_o.set_unit("Hz")
    # pitch_o.set_tolerance(tolerance)

    print("*** starting recording")
    while True:
        try:
            audiobuffer = stream.read(buffer_size)
            signal = np.frombuffer(audiobuffer, dtype=np.float32)

            pitch = pitch_o(signal)[0]
            confidence = pitch_o.get_confidence()

            print("{} / {}".format(pitch, confidence))

            # if outputsink:
            #     outputsink(signal, len(signal))

            # if record_duration:
            #     total_frames += len(signal)
            #     # if record_duration * samplerate < total_frames:
            #     #     break
        except KeyboardInterrupt:
            print("*** Ctrl+C pressed, exiting")
            break

    print("*** done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()


def driver():
    frequency_demo_aubio()
    # test_input_devices()


driver()
