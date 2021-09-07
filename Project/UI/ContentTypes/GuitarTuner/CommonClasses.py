import threading
import time
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton

from Project.Tuner import main_tuner, better_tuner
from Project.UI.CommonWidgets.FontFactory import font_factory


class GuitarTunerButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(GuitarTunerButton, self).__init__()
        self.Flag = 0
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.clicked.connect(self.start_tuner)
        self.set_button()


    def start_tuner(self):
        print("start tuner")
        print(self.sender().Flag)
        if self.sender().Flag == 0:
            self.sender().Flag = 1
            self.flag = False
            self.thread = threading.Thread(target=self.get_tuner)
            self.thread.start()
            #self.sender().setText('Recording')
        elif self.sender().Flag == 1:
            self.flag = True
            self.sender().Flag = 0
            #self.close_tape(self.stream, self.p)
            #self.sender().setText('RECORD')

    def get_tuner(self):
        while True:
            print(self.flag)
            if self.flag:
                break
            better_tuner()
            #print(chord)

    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font_factory("14"))

    def change_note(self, note, string_num):
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)



