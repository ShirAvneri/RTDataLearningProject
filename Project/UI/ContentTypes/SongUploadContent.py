import threading
import time

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtGui import QTextCursor, QColor
from PySide6.QtWidgets import QPlainTextEdit

from Project.ChordDetector.ChordDetection.chroma_chord_detection import chord_detection_prefilepath
from Project.UI.CommonWidgets.CommonButtons import FilePickerButton
from Project.UI.ContentComponent import Content
from Project.UI.ContentTypes.ChordDetection.CommonClasses import ChordAnalyzingButton


class SongUploadContent(Content):
    def __init__(self, is_full_screen):
        super(SongUploadContent, self).__init__(is_full_screen)
        self.counter = 1
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
        self.path = "a"
        self.upload_button = FilePickerButton()
        self.buttons.append(self.upload_button)
        self.upload_button.setParent(self)
        self.upload_button.init_style("MetronomeController", 625, 150)
        self.analyze_button = ChordAnalyzingButton(640, 400)
        self.analyze_button.setParent(self)
        self.analyze_button.clicked.connect(self.analyze)
        self.thread = None
        self.process = None
        self.stream = None
        self.p = None
        self.flag = False
        self.finish_analyze = False
        self.analyze_button.path = self.path

    def analyze(self):

        if self.upload_button.path == "":
            self.chord_text.setStyleSheet("QPlainTextEdit {color: red;}");
            self.chord_text.setPlainText("Please, choose song")
            return
        else:
            self.chord_text.setStyleSheet("QPlainTextEdit {color: black;}");
            self.chord_text.setPlainText("Detected Chord:")
            self.finish_analyze = True

            self.analyzing_sign_thread = AnalyzingSignClass(self)
            self.analyzing_sign_thread.start()
            self.analyzing_sign_thread.any_signal.connect(self.update_text)
            self.analyzing_sign_thread.finish_analyze = self.finish_analyze

            self.thread = AnalyzingThreadClass(self)
            self.thread.start()
            self.thread.path = self.upload_button.path[0]
            self.thread.any_signal.connect(self.insert_chords)

    @Slot(str)
    def update_text(self, text):
        self.chord_text.clear()
        self.chord_text.setPlainText(text)

    @Slot(object)
    def insert_chords(self, chord_list):
        self.finish_analyze = False
        self.chord_text.clear()
        print('inserting chords')
        count = 0
        for x in range(len(chord_list)):
            count += 1
            self.chord_text.moveCursor(QTextCursor.EndOfBlock)
            self.chord_text.insertPlainText(str(chord_list[x]) + '                      ')
            if count == 4:
                self.chord_text.moveCursor(QTextCursor.End)
                self.chord_text.insertPlainText('\n\n')
                count = 0


class AnalyzingSignClass(QThread):

    any_signal = Signal(str)

    def __init__(self, MySongUploadContent, parent=None, index=0):
        super(AnalyzingSignClass, self).__init__(parent)
        self.MySongUploadContent = MySongUploadContent
        self.finish_analyze = True

    def run(self):
        text = "Analyzing. "
        count = 0
        while self.MySongUploadContent.finish_analyze:
            if count == 2:
                text = "Analyzing. "
                self.any_signal.emit(text)
                count = 0
            else:
                text += '. '
                self.any_signal.emit(text)
                count += 1
            self.msleep(400)


class AnalyzingThreadClass(QThread):

    any_signal = Signal(object)

    def __init__(self, MySongUploadContent, parent=None, index=0):
        super(AnalyzingThreadClass, self).__init__(parent)
        self.path = ""
        self.MySongUploadContent = MySongUploadContent

    def run(self):
        chord_list = chord_detection_prefilepath(self.path)
        self.MySongUploadContent.finish_analyze = False
        self.sleep(1)
        self.any_signal.emit(chord_list)
