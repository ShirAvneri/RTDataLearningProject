import threading

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
        self.analyze_button.path = self.path

    def analyze(self):

        if self.upload_button.path == "":
            self.chord_text.setStyleSheet("QPlainTextEdit {color: red;}");
            self.chord_text.setPlainText("Please, choose song")
            return
        else:
            print("HERE")
            self.chord_text.setStyleSheet("QPlainTextEdit {color: black;}");
            self.chord_text.setPlainText("Detected Chord:")
            self.finish_analyze=True
            #self.thread = threading.Thread(target=self.detect_chord_in_analyze)
            #self.thread.start()
            self.analyze_thread = threading.Thread(target=self.write_analyze)
            self.analyze_thread.start()



    def write_analyze(self):
        self.chord_text.appendPlainText("\n\n")
        self.chord_text.appendPlainText("Analyze")
        count = 0
        # cursor = self.chord_text.textCursor()
        while self.finish_analyze:
            if count == 3:
                self.chord_text.setPlainText("Detected Chord:\n\nAnalyze")
                count = 0
            self.chord_text.appendPlainText(". ")
            count += 1

    def detect_chord_in_analyze(self):
        return_list = chord_detection_prefilepath(self.upload_button.path[0])
        #self.chord_text.moveCursor(QTextCursor.End)
        self.finish_analyze=False
        self.chord_text.insertPlainText('\n')
        self.chord_text.appendPlainText(str(return_list))

        count = 0
        # for x in range(len(return_list)):
        #     print("1")
        #     count += 1
        #     self.chord_text.moveCursor(QTextCursor.EndOfBlock)
        #     print("2")
        #     self.chord_text.insertPlainText(str(return_list[x]) + '                      ')
        #     print("3")
        #     if count == 4:
        #         print("4")
        #         self.chord_text.moveCursor(QTextCursor.End)
        #         self.chord_text.insertPlainText('\n\n')
        #         count = 0
        #         print("5")
        self.counter += 1
        print("thread END")
