from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content
from Project.UI.ContentTypes.ChordDetection.CommonClasses import RecordingButton
import threading


class ChordDetectionContent(Content):
    def __init__(self):
        super(ChordDetectionContent, self).__init__()
        self.buttons = []
        self.record_button = StartStopButton(self.start_record, self.stop_record)
        self.buttons.append(self.record_button)
        self.record_button.setParent(self)
        self.record_button.init_style("MetronomeController", 250, 400)
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
            if self.flag:
                chord_detection.close_stream(self.stream, self.p)
                print('recording complete')
                break
            chord = chord_detection.get_chord_from_stream(self.stream, self.p)
            print(chord)

    def start_record(self):
        print('opening stream...')
        self.flag = False
        self.thread = threading.Thread(target=self.get_chords)
        self.thread.start()

    def stop_record(self):
        self.flag = True


