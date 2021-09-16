import threading
import time

from PyQt5.QtGui import QIcon, QPixmap
from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import QPushButton, QLabel
from Project import Constants
from Project.Tuner import better_tuner
from Project.UI.CommonWidgets.CommonFonts import create_font


class GuitarTunerButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(GuitarTunerButton, self).__init__()
        self.Flag = 0
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.style = "qproperty-icon: url(); border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.style_red_up = "qproperty-icon: url(./UI/Images/arrow_up.png);qproperty-iconSize: 30px; border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color:  #ff1a1a; " \
                         "border-radius: 25px; "
        self.style_red_down = "qproperty-icon: url(./UI/Images/arrow_down.png);qproperty-iconSize: 30px; border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color:  #ff1a1a; " \
                            "border-radius: 25px; "
        self.style_green = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color:  green; " \
                           "border-radius: 25px; "
        self.style_yellow_up = "qproperty-icon: url(./UI/Images/arrow_up.png);qproperty-iconSize: 30px; border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: yellow; "\
                            "border-radius: 25px; "
        self.style_yellow_down = "qproperty-icon: url(./UI/Images/arrow_down.png);qproperty-iconSize: 30px; border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: yellow; " \
                               "border-radius: 25px; "
        #self.setIcon(QIcon("./UI/Images/Microphone.png"))
        #self.setIconSize(QSize(5, 5))
        self.clicked.connect(self.start_tuner)
        self.set_button()



    def start_tuner(self):
        self.parent().zero_all(self)
        print("start tuner")
        print(self.sender().Flag)
        #self.parent().zero_all()
        if self.sender().Flag == 0:
            print("START")
            self.sender().Flag = 1
            self.flag = False
            self.thread = threading.Thread(target=self.get_tuner)
            self.thread.start()
            # self.thread.kill()
        elif self.sender().Flag == 1:
            print("STOPPPPPP")
            self.flag = True
            # self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
            #self.setText(self.note)
            self.sender().Flag = 0
            # self.setEnabled(True)

    def get_tuner(self):
        while True:
            # print(self.flag)
            if self.flag:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
                break
            # self.setEnabled(False)
            better_tuner()
            # self.setEnabled(True)
            # print("***********************")
            print(Constants.ClosetNote)
            if Constants.ClosetNote[0] < self.note[0]:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_red_up + " }")
                print("in reddddddddddd")
                self.setText("")
                if self.flag:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
                    self.setText(self.note)
                    break
            elif Constants.ClosetNote[0] == self.note[0]:
                # self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_OK + " }")
                number_in_cur_note = Constants.ClosetNote[1]
                number_in_note = self.note[1]
                if number_in_note == "#":
                    number_in_note = self.note[2]
                if number_in_cur_note == "#":
                    number_in_note = Constants.ClosetNote[2]
                if number_in_cur_note < number_in_note:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_yellow_up + " }")
                    self.setText("")
                elif number_in_cur_note == number_in_note:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_green + " }")
                    self.setText(self.note)
                else:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_yellow_down + " }")
                    self.setText("")

                print("in Ylow")

            else:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_red_down + " }")
                print("in green")
                self.setText("")
        print("end tuner")
        self.setText(self.note)

    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(create_font(size=14))


    def change_note(self, note, string_num):
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
