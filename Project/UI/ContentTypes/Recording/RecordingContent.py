import threading
import time
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QFileDialog, QLabel
from Project import Recording
from Project.UI.CommonWidgets.WidgetsFactory import font_factory
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content


class RecordingContent(Content):
    def __init__(self):
        super(RecordingContent, self).__init__()
        self.is_recording = False
        self.used_threads = []
        self.recording_button = StartStopButton(self.start_recording, self.stop_recording)
        self.recording_button.init_style("Recording Button", 400, 30)
        self.recording_button.setParent(self)

        self.timer_label = QLabel()
        self.timer_label.setParent(self)
        self.timer_label.setText("00:00:00")
        self.timer_label.setGeometry(QRect(40, 520, 250, 30))
        self.timer_label.setFont(font_factory(size=18))

        microphone_image = QLabel(self)
        microphone_image.setObjectName("MicrophoneImageLabel")
        microphone_image.setGeometry(QRect(175, 30, 250, 530))
        microphone_image.setStyleSheet("QLabel#MicrophoneImageLabel { border-image: url(./UI/Images/Microphone.png) "
                                       "0 0 0 stretch stretch; }")
        microphone_image.setParent(self)

    def start_recording(self):
        self.is_recording = True
        recording_thread = threading.Thread(target=self.get_audio_stream)
        self.used_threads.append(recording_thread)
        timer_thread = threading.Thread(target=self.start_timer)
        self.used_threads.append(timer_thread)
        recording_thread.start()
        timer_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.timer_label.setText("00:00:00")
        for used_thread in self.used_threads:
            used_thread.join()

    def start_timer(self):
        time_start = time.time()
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
        fileName = QFileDialog.getSaveFileName(self, "Save F:xile",
                                               "/home/jana/untitled.png",
                                               "Images (*.png *.xpm *.jpg)")

    def get_audio_stream(self):
        stream, p = Recording.open_stream()
        frames = []
        while self.is_recording:
            Recording.get_stream(stream, p, frames)
        Recording.end_stream(stream, p, frames)
        print("audio saved")
