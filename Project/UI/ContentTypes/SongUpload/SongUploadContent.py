from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.FilePickerButton import FilePickerButton
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content
from Project.UI.ContentTypes.ChordDetection.CommonClasses import RecordingButton, ChordAnalyzingButton
from Project.ChordDetector.ChordDetection.chroma_chord_detection import chord_detection_prefilepath
import threading


class SongUploadContent(Content):
    def __init__(self):
        super(SongUploadContent, self).__init__()
        self.buttons = []
        self.path = "a"
        self.upload_button = FilePickerButton()
        self.buttons.append(self.upload_button)
        self.upload_button.setParent(self)
        self.upload_button.init_style("MetronomeController", 250, 400)
        self.analyze_button = ChordAnalyzingButton(200, 400)
        self.analyze_button.setParent(self)
        self.analyze_button.clicked.connect(self.analyze)
        self.thread = None
        self.process = None
        self.stream = None
        self.p = None
        self.flag = False
        self.analyze_button.path = self.path
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(130, 50, 260, 500))
        # text.setText('note detected: ')
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(220, 50, 260, 500))
        # text.setText('NOTE')

    def analyze(self):
        print(self.upload_button.path[0])
        if self.upload_button.path == "":
            return
        else:
            chord_detection_prefilepath(self.upload_button.path[0])

