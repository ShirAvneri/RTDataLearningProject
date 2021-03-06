import pyaudio
import wave

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QFileDialog

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recorded.wav"

def open_stream():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    return stream, p

def get_stream(stream, p,frames):

    data = stream.read(CHUNK)
    frames.append(data)

    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        #data = stream.read(CHUNK)
        #frames.append(data)


def end_stream(stream, p, frames, file_name):

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

    #filename, _ = QFileDialog.getSaveFileName(
     #   self,
      ## '',
        #"ReStructuredText Files (*.rst *.txt)"
    #)
    wf.close()