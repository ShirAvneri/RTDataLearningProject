import threading
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton

from Project import Constants
from Project.Tuner import better_tuner
from Project.UI.CommonWidgets.WidgetsFactory import font_factory


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
        self.style_red = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: red; " \
                      "border-radius: 25px; "
        self.style_green = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: green; " \
                         "border-radius: 25px; "
        self.style_OK = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: yellow; " \
                           "border-radius: 25px; "
        self.style_OK_up = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color:  #808000; " \
                        "border-radius: 25px; "
        self.style_OK_down = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color:  #ffff66; " \
                        "border-radius: 25px; "
        self.clicked.connect(self.start_tuner)
        self.set_button()


    def start_tuner(self):
        print("start tuner")
        print(self.sender().Flag)
        if self.sender().Flag == 0:
            print("START")
            self.sender().Flag = 1
            self.flag = False
            self.thread = threading.Thread(target=self.get_tuner)
            self.thread.start()
            #self.thread.kill()
        elif self.sender().Flag == 1:
            print("STOPPPPPP")
            self.flag = True
            #self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
            self.sender().Flag = 0


    def get_tuner(self):
        while True:
            #print(self.flag)
            if self.flag:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
                break
            better_tuner()
            #print("***********************")
            print(Constants.ClosetNote)
            if Constants.ClosetNote[0]<self.note[0]:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_red + " }")
                print("in red")
                if self.flag:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
                    break
            elif Constants.ClosetNote[0] == self.note[0]:
                #self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_OK + " }")
                number_in_cur_note = Constants.ClosetNote[1]
                number_in_note = self.note[1]
                if number_in_note == "#":
                    number_in_note = self.note[2]
                if number_in_cur_note == "#":
                    number_in_note = Constants.ClosetNote[2]
                if number_in_cur_note < number_in_note:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_OK_up + " }")
                elif number_in_cur_note == number_in_note:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_OK + " }")
                else:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_OK_down + " }")


                print("in Ylow")

            else:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_green + " }")
                print("in green")
        print("end tuner")

    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font_factory(size=14))

    def change_note(self, note, string_num):
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)



