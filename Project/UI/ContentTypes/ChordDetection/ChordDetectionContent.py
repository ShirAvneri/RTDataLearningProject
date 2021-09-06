# from Project.ChordDetector import chord_detection
from Project.ChordDetector import chord_detection
from Project.UI.Content import Content
from Project.UI.ContentTypes.Recording.CommonClasses import RecordingButton
import threading


class ChordDetectionContent(Content):
    def __init__(self):
        super(ChordDetectionContent, self).__init__()
        self.buttons = []
        record_button = RecordingButton(300, 100)
        self.buttons.append(record_button)
        record_button.setParent(self)
        record_button.clicked.connect(self.record)
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

    def get_chords(self):
        self.stream, self.p = chord_detection.open_stream()
        while True:

            print(self.flag)
            if self.flag:
                break
            chord = chord_detection.get_chord_from_stream(self.stream, self.p)
            print(chord)

    def record(self, btn):
        if self.sender().text() == "Record":
            self.flag = False
            self.thread = threading.Thread(target=self.get_chords)
            self.thread.start()
            self.sender().setText('Recording')
        elif self.sender().text() == "Recording":
            self.flag = True
            chord_detection.close_stream(self.stream, self.p)
            self.sender().setText('Record')
