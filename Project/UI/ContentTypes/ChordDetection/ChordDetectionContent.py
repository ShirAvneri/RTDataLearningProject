from PySide6.QtCore import QRect, Signal, QThread, Qt, Slot
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QPlainTextEdit

from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.CommonButtons import StartStopButton
from Project.UI.CommonWidgets.CommonFonts import create_font
from Project.UI.CommonWidgets.CommonLabels import Label
from Project.UI.ContentComponent import Content


class ChordDetectionContent(Content):
    def __init__(self, is_full_screen):
        super(ChordDetectionContent, self).__init__(is_full_screen)

        self.count = 0
        text = "Detected Chord:"
        self.chord_text = QPlainTextEdit()
        self.chord_text.setParent(self)
        self.chord_text.setMinimumWidth(450)
        self.chord_text.setMinimumHeight(550)
        self.chord_text.appendPlainText(text)
        self.chord_text.setReadOnly(True)
        self.chord_label = QLabel(self)
        self.chord_label.setGeometry(QRect(0, 0, 1350, 400))
        self.chord_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.chord_label.setFont(create_font(size=150, bold=True))
        self.chord_label.setStyleSheet("color: #972c2c")
        self.chord_label.setText("")
        self.record_button = StartStopButton(self.start_record, self.stop_record)
        self.record_button.setParent(self)
        self.record_button.init_style("MetronomeController", 625, 400)
        self.thread = None
        self.stream = None
        self.pyAudio = None
        self.close_stream_flag = False

    def start_record(self):
        print('opening stream...')
        self.thread = ThreadClass(self)
        self.close_stream_flag = False
        self.chord_text.clear()
        self.thread.start()
        self.thread.any_signal.connect(self.append_text)

    def stop_record(self):
        self.close_stream_flag = True

    @Slot(str)
    def append_text(self, text):
        self.chord_label.setText(text)
        self.chord_text.moveCursor(QTextCursor.End)
        self.count += 1
        self.chord_text.insertPlainText(text + '                      ')
        if self.count == 4:
            self.chord_text.moveCursor(QTextCursor.End)
            self.chord_text.insertPlainText('\n\n')
            self.count = 0


class ThreadClass(QThread):

    any_signal = Signal(str)

    def __init__(self, MyChordDetectionContent, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.MyChordDetectionContent = MyChordDetectionContent

    def run(self):
        self.stream, self.pyAudio = chord_detection.open_stream()
        while True:
            if self.MyChordDetectionContent.close_stream_flag:
                chord_detection.close_stream(self.stream, self.p)
                print('recording complete')
                break
            chord = chord_detection.get_chord_from_stream(self.stream, self.p)
            self.any_signal.emit(chord)

