import os
import threading
import time
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QFileDialog, QLabel

from Project import Recording
from Project.UI.CommonWidgets.CommonButtons import StartStopButton
from Project.UI.CommonWidgets.CommonFonts import create_font
from Project.UI.ContentComponent import Content


class RecordingContent(Content):
    def __init__(self, is_full_screen):
        super(RecordingContent, self).__init__(is_full_screen)
        self.is_recording = False
        self.used_threads = []
        self.recording_button = StartStopButton(self.start_recording, self.stop_recording)
        self.recording_button.init_style("Recording Button", 550, 30)
        self.recording_button.setParent(self)
        self.stream = None
        self.p = None
        self.frames = []
        self.timer_label = QLabel()
        self.timer_label.setParent(self)
        self.timer_label.setText("00:00:00")
        self.timer_label.setGeometry(QRect(40, 520, 250, 30))
        self.timer_label.setFont(create_font(size=18))

        microphone_image = QLabel(self)
        microphone_image.setObjectName("MicrophoneImageLabel")
        microphone_image.setGeometry(QRect(315, 30, 250, 530))
        microphone_image.setStyleSheet("QLabel#MicrophoneImageLabel { border-image: url(./UI/Images/Microphone.png) "
                                       "0 0 0 stretch stretch; }")
        microphone_image.setParent(self)

        self.count_down_label = QLabel()
        self.count_down_label.setParent(self)
        self.count_down_label.setText("")
        self.count_down_label.setGeometry(QRect(450, 300, 90, 30))
        self.count_down_label.setFont(create_font(size=18))
        self.count_down_label.setStyleSheet("QLabel { color : red; }");

    def start_recording(self):
        self.is_recording = True
        recording_thread = threading.Thread(target=self.get_audio_stream)
        self.used_threads.append(recording_thread)
        recording_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.timer_label.setText("00:00:00")
        for used_thread in self.used_threads:
            used_thread.join()
        file_name = self.save_file()
        print("*****************")
        print(file_name[0])
        if not file_name[0]:
            file_name = "/Grabge.py/"
            file_name = str(os.path.abspath(os.curdir)).replace("\\", "/") + file_name
        Recording.end_stream(self.stream, self.p, self.frames, file_name[0])
        self.frames = []

    def start_timer(self):
        self.setEnabled(False)
        self.count_down_label.setText("3")
        time.sleep(1)
        self.count_down_label.setText("2")
        time.sleep(1)
        self.count_down_label.setText("1")
        time.sleep(1)
        self.count_down_label.setText("")
        time_start = time.time()
        self.setEnabled(True)
        seconds = 0
        minutes = 0
        hours = 0
        while self.is_recording or hours > 10:
            self.timer_label.setText("{hours:0>2}:{minutes:0>2}:{seconds:0>2}".
                                     format(hours=hours, minutes=minutes, seconds=seconds))
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
                seconds = 0
            if minutes >= 60:
                hours += 1
                minutes = 0

        if hours > 2:
            self.stop_recording()

    def save_file(self):
        return QFileDialog.getSaveFileName(self, "Save F:xile",
                                           "recored_file.wav",
                                           "sound (*.wav)")

    def get_audio_stream(self):
        self.stream, self.p = Recording.open_stream()
        timer_thread = threading.Thread(target=self.start_timer)
        self.used_threads.append(timer_thread)
        timer_thread.start()
        while self.is_recording:
            Recording.get_stream(self.stream, self.p, self.frames)

        print("audio saved")
