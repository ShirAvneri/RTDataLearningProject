import threading
import wave
import pyaudio
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton

from Project import Recording


class RecordingButton(QPushButton):
    def __init__(self, x_pos, y_pos):
        super(RecordingButton, self).__init__()
        self.setObjectName("Recording Button")
        self.x = x_pos
        self.y = y_pos
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.clicked.connect(self.record_in_recording)
        self.set_button()

    def set_button(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + "Recording  Button" + " { " + self.style + " }")
        self.setText("RECORD")
        self.setFont(font)

    def record_in_recording(self, btn):
        if self.sender().text() == "RECORD":
            self.flag = False
            self.thread = threading.Thread(target=self.get_tape)
            self.thread.start()
            self.sender().setText('Recording')
        elif self.sender().text() == "Recording":
            self.flag = True
            #self.close_tape(self.stream, self.p)
            self.sender().setText('RECORD')

    def get_tape(self):
        self.stream, self.p = Recording.open_stream()
        frames = []
        while True:
            print(self.flag)
            if self.flag:
                break
            Recording.get_stream(self.stream, self.p, frames)
            #print(chord)
        Recording.end_stream(self.stream, self.p, frames)

    def get_Tape(self):
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

        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            if self.flag:
                break
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()