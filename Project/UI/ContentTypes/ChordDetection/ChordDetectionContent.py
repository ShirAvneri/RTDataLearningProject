from PyQt5.QtCore import pyqtSignal, QThread, pyqtSlot
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QPlainTextEdit

from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.CommonButtons import StartStopButton
from Project.UI.ContentComponent import Content


class ChordDetectionContent(Content):
    def __init__(self, is_full_screen):
        super(ChordDetectionContent, self).__init__(is_full_screen)

        self.count = 0
        self.labelLists = []
        self.labelList = []
        self.buttonList = []

        text = "Detected Chord:"
        self.chord_text = QPlainTextEdit()
        self.chord_text.setParent(self)
        self.chord_text.setMinimumWidth(450)
        self.chord_text.setMinimumHeight(550)

        # self.QPlainTextEdit.setGeometry(QRect(50, 50, 50, 50))

        self.chord_text.appendPlainText(text)
        # self.chord_text.setPlainText("**********************")
        self.chord_text.setReadOnly(True)

        self.buttons = []
        self.record_button = StartStopButton(self.start_record, self.stop_record)
        self.buttons.append(self.record_button)
        self.record_button.setParent(self)
        self.record_button.init_style("MetronomeController", 625, 225)
        self.thread = None
        self.process = None
        self.stream = None
        self.p = None
        self.flag = False
        self.counter = 1

    def get_chords(self):
        self.chord_text.appendPlainText("Iteration number:"+str(self.counter))
        self.counter+=1
        self.stream, self.p = chord_detection.open_stream()
        while True:
            if self.flag:
                chord_detection.close_stream(self.stream, self.p)
                print('recording complete')
                break
            chord = chord_detection.get_chord_from_stream(self.stream, self.p)
            print(chord)
            text = '%s' % chord
            self.chord_text.appendPlainText(text)
            print(len(self.labelList), self.count)
            for i in range(1):
                self.labelList.append(QLabel("Label "))
                self.buttonList.append(QPushButton("Btn "))

            #self.formLayout.addRow(self.labelList[self.count - 1], QPushButton("Btn "))

    def start_record(self):
        print('opening stream...')
        self.thread = ThreadClass(self)
        self.thread.start()
        self.thread.any_signal.connect(self.parent().my_function)

    def stop_record(self):
        self.flag = True

    def append_text(self, text):
        self.chord_text.appendPlainText(text)


class ThreadClass(QThread):
    any_signal = pyqtSignal(str)

    def __init__(self, ChordDetectionContent, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.ChordDetectionContent = ChordDetectionContent

    def run(self):
        # print("chord")
        self.stream, self.p = chord_detection.open_stream()
        while True:
            if self.ChordDetectionContent.flag:
                chord_detection.close_stream(self.stream, self.p)
                print('recording complete')
                break
            chord = chord_detection.get_chord_from_stream(self.stream, self.p)
            self.any_signal.emit(chord)
