from Project.ChordDetector import chord_detection
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.ContentComponent import Content

from Project.UI.ContentTypes.ChordDetection.CommonClasses import RecordingButton
import threading
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QFormLayout, QGroupBox, QLabel, QScrollArea, \
    QVBoxLayout
import sys
from PySide6 import QtGui


class ChordDetectionContent(Content):
    def __init__(self, is_full_screen):
        super(ChordDetectionContent, self).__init__(is_full_screen)

        self.count = 0

        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox("This is a groupBox")
        self.labelLists = []
        self.labelList = []
        self.buttonList = []

        # for i in range (5):
        #     labelList.append(QLabel("Label "))
        #     buttonList.append(QPushButton("Btn "))
        #     formLayout.addRow(labelList[i], buttonList[i])

        self.groupBox.setLayout(self.formLayout)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.groupBox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(400)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

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

    def get_chords(self):
        self.stream, self.p = chord_detection.open_stream()
        while True:
            if self.flag:
                chord_detection.close_stream(self.stream, self.p)
                print('recording complete')
                break
            chord = chord_detection.get_chord_from_stream(self.stream, self.p)
            self.count += 1
            # self.labelList.append(QLabel(chord))
            print(len(self.labelList), self.count)
            for i in range(1):
                self.labelList.append(QLabel("Label "))
                self.buttonList.append(QPushButton("Btn "))
                self.formLayout.insertRow(self.count - 1, self.labelList[i], self.buttonList[i])
            # self.formLayout.addRow(self.labelList[self.count - 1], QPushButton("Btn "))

    def start_record(self):
        print('opening stream...')
        self.flag = False
        self.thread = threading.Thread(target=self.get_chords)
        self.thread.start()

    def stop_record(self):
        self.flag = True
