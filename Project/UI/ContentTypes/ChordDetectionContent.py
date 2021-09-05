from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QPushButton

#from Project.ChordDetector import chord_detection
from Project.ChordDetector import chord_detection
from Project.UI.Content import Content
from Project.UI.ContentTypes.Common import GuitarTunerButton, RecordingButton


class ChordDetectionContent(Content):
    # def __init__(self):
    #     super(ChordDetectionContent, self).__init__()
    #     chord_image = QLabel(self)
    #     chord_image.setObjectName("GuitarImageLabel")
    #     chord_image.setGeometry(QRect(500, 50, 260, 500))
    #     chord_image.setText("hello world")
    #     record_button = QPushButton("record")
    #     record_button = Recording
    #     record_button.setGeometry(QRect(170, 50, 260, 500))
    #     record_button.clicked.connect(self.record(record_button))
    #
    # def record(self, btn):
    #     btn.setText("changed")
    #     #chord_detection.clicked()

    def __init__(self):
        super(ChordDetectionContent, self).__init__()
        self.buttons = []
        record_button = RecordingButton(300, 100)
        self.buttons.append(record_button)
        record_button.setParent(self)
        record_button.clicked.connect(self.record)
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(130, 50, 260, 500))
        # text.setText('note detected: ')
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(220, 50, 260, 500))
        # text.setText('NOTE')

    def record(self, btn):
        print(self.sender().text())
        if self.sender().text() == "Record":
            chord_detection.clicked2()
            self.sender().setText('clicked')
