from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.FilePickerButton import FilePickerButton
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content
from Project.UI.ContentTypes.ChordDetection.CommonClasses import RecordingButton
import threading


class SongUploadContent(Content):
    def __init__(self):
        super(SongUploadContent, self).__init__()
        self.buttons = []
        self.path = ""
        self.upload_button = FilePickerButton()
        self.buttons.append(self.upload_button)
        self.upload_button.setParent(self)
        self.upload_button.init_style("MetronomeController", 250, 400)
        self.thread = None
        self.process = None
        self.stream = None
        self.p = None
        self.flag = False
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(130, 50, 260, 500))
        # text.setText('note detected: ')
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(220, 50, 260, 500))
        # text.setText('NOTE')




