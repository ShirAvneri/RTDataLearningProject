import threading

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QFileDialog, QLabel

from Project import Recording
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content


class RecordingContent(Content):
    def __init__(self):
        super(RecordingContent, self).__init__()
        self.is_recording = False
        self.button = StartStopButton(self.start_recording, self.stop_recording)
        self.button.init_style("Recording Button", 400, 30)
        self.button.setParent(self)
        microphone_image = QLabel(self)
        microphone_image.setObjectName("MicrophoneImageLabel")
        microphone_image.setGeometry(QRect(175, 30, 250, 530))
        microphone_image.setStyleSheet("QLabel#MicrophoneImageLabel { border-image: url(./UI/Images/Microphone.png) 0 "
                                       "0 0 stretch stretch; }")
        microphone_image.setParent(self)

    def start_recording(self):
        self.is_recording = True
        thread = threading.Thread(target=self.get_tape)
        thread.start()

    def stop_recording(self):
        self.is_recording = False

    def save_file(self):
        fileName = QFileDialog.getSaveFileName(self, "Save F:xile",
                                               "/home/jana/untitled.png",
                                               "Images (*.png *.xpm *.jpg)")

    def get_tape(self):
        stream, p = Recording.open_stream()
        frames = []
        while self.is_recording:
            Recording.get_stream(stream, p, frames)
        Recording.end_stream(stream, p, frames)
        print("end get tape")
