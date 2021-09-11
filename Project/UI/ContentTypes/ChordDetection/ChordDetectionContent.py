from PySide6.QtCore import QRect

from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content
from Project.UI.ContentTypes.ChordDetection.CommonClasses import RecordingButton, PlainText
import threading
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QFormLayout, QGroupBox, QLabel, QScrollArea, \
    QVBoxLayout, QPlainTextEdit
import sys
from PySide6 import QtGui

class ChordDetectionContent(Content):
    def __init__(self):
        super(ChordDetectionContent, self).__init__()

        self.count = 0
        #self.vBOX=QVBoxLayout()
        #self.chord_text=QPlainTextEdit()
        #self.formLayout = QFormLayout()
        #self.groupBox = QGroupBox("This is a groupBox")
        self.labelLists = []
        self.labelList = []
        self.buttonList = []

        #self.plain_text=PlainText(50,50)
        #self.plain_text.parent=self
        #self.chord_text = QPlainTextEdit()


        self.vBOX = QVBoxLayout()

        text = "Detected Chord:"
        self.chord_text = QPlainTextEdit()
        self.vBOX.setGeometry(QRect(50,50,50,50))

        self.chord_text.appendPlainText(text)
        #self.chord_text.setPlainText("**********************")
        self.chord_text.setReadOnly(True)
        self.vBOX.addWidget(self.chord_text)
        self.setLayout(self.vBOX)

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
        self.counter = 1

    def get_chords(self):
        #print("chord")
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
            text='%s' % chord
            self.chord_text.appendPlainText(text)
            print(len(self.labelList), self.count)
            for i in range (1):
                self.labelList.append(QLabel("Label "))
                self.buttonList.append(QPushButton("Btn "))
            #self.formLayout.addRow(self.labelList[self.count - 1], QPushButton("Btn "))

    def start_record(self):
        print('opening stream...')
        self.flag = False
        self.thread = threading.Thread(target=self.get_chords)
        self.thread.start()

    def stop_record(self):
        self.flag = True


