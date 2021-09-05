#from ChordDetection.chroma_chord_detection import chord_detection_filepath, chord_detection_prefilepath
from Project.ChordDetector.ChordDetection.chroma_chord_detection import chord_detection_filepath, chord_detection_prefilepath

import numpy as np
import pyaudio # Soundcard audio I/O access library
from tkinter import *
import librosa as lb
import wave

FORMAT = pyaudio.paInt16
CHUNK = 1024
WIDTH = 2
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'output.wav'


def open_stream():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    return stream, p


def get_chord_from_stream(stream, p):
    itterations = 0
    chords = []
    while True:
        frames = []

        for i in range(0, int(RATE / CHUNK * 0.2)):
            data = stream.read(CHUNK)
            frames.append(data)

        # stream.stop_stream()
        # stream.close()
        # p.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(p.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        chord_name = chord_detection_filepath("output.wav")

        chords.append(str(chord_name))
        itterations += 1
        if itterations == 13:
            itterations = 0
            print("Estimated chord: " + max(chords, key=chords.count))
            return max(chords, key=chords.count)
            # print(chords)
            chords.clear()


def close_stream(stream, p):
    stream.stop_stream()
    stream.close()
    p.terminate()


def clicked():
    print("in clicked")
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    itterations = 0
    chords = []
    print("Recording:")
    while True:
        frames = []

        for i in range(0, int(RATE / CHUNK * 0.2)):
            data = stream.read(CHUNK)
            frames.append(data)

        #stream.stop_stream()
        #stream.close()
        #p.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(p.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        chord_name = chord_detection_prefilepath("EE7.wav")

        chords.append(str(chord_name))
        itterations += 1
        if itterations == 13:
            itterations = 0
            print("Estimated chord: " + max(chords, key=chords.count))
            #print(chords)
            chords.clear()


def clicked2():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    itterations = 0
    chords = []
    print("Recording:")
    while True:
        frames = []

        for i in range(0, int(RATE / CHUNK * 0.2)):
            data = stream.read(CHUNK)
            frames.append(data)


        # stream.stop_stream()
        # stream.close()
        # p.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(p.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        chord_name = chord_detection_filepath("output.wav")

        chords.append(str(chord_name))
        itterations += 1
        if itterations == 13:
            itterations = 0
            print("Estimated chord: " + max(chords, key=chords.count))
            # print(chords)
            chords.clear()

