import pyaudio
import sys
import aubio
import numpy as np
from tkinter import *


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


def click_button_tkinter_1():

    # if you want to submit a form or whatever, this is a great tool!
    root = Tk()

    def click_handler():
        myLabel = Label(root, text="Clicked!!")
        myLabel.pack()

    # we do not use the paranthesis for command buttons!
    button = Button(
        root, text="click Me!", command=click_handler, fg="blue", bg="green"
    )
    button.pack()

    root.mainloop()


def input_box_tkinter_2():
    root = Tk()

    entry = Entry(root, width=50, bg="yellow")
    entry.pack()
    entry.insert(0, "Enter name? ")  # puts text inside input box

    def click_handler():
        label = Label(
            root, text="Hello " + entry.get()
        )  # entry get will get the input in the box
        label.pack()

    button = Button(root, text="click me ", command=click_handler)
    button.pack()

    root.mainloop()


def simple_calculator_tkinter_3():
    root = Tk()
    root.title("Simple Calculator")

    entry = Entry(root, width=35, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_add(number):
        current = entry.get() 
        entry.insert(0, "" + current + number)

    # Define Buttons
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))

    button_adding = Button(root, text="+", padx=40, pady=20, command=button_add)
    button_equals = Button(root, text="=", padx=40, pady=20, command=button_add)
    button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_add)

    # Putting buttons on the screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_adding.grid(row=4, column=1)
    button_equals.grid(row=4, column=2)
    button_clear.grid(row=5, column=0)

    entry.insert(0, " ")

    root.mainloop()


def driver():
    # frequency_demo_aubio()
    # test_input_devices()
    # click_button_tkinter_1()
    # input_box_tkinter_2()
    simple_calculator_tkinter_3()


driver()
