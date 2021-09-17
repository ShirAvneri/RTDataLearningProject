import threading
import time

from PyQt5.QtGui import QIcon, QPixmap
from PySide6.QtCore import QRect, QSize, QThread, Signal, Slot
from PySide6.QtWidgets import QPushButton, QLabel
from Project import Constants
from Project.Tuner import better_tuner
from Project.UI.CommonWidgets.CommonFonts import create_font

notes = ['StartBuffer', 'A1', 'A#1', 'B1', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1',
         'A2', 'A#2', 'B2', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2',
         'A3', 'A#3', 'B3', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3',
         'A4', 'A#4', 'B4', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4',
         'A5', 'A#5', 'B5', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5',
         'A6', 'A#6', 'B6', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'EndBuffer']


class GuitarTunerButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(GuitarTunerButton, self).__init__()
        self.is_clicked = False
        self.is_tuning = False
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
        self.clicked.connect(self.start_tuner)
        self.set_button()



    def start_tuner(self):
        self.parent().zero_all(self)
        if not self.sender().is_clicked:
            self.sender().is_clicked = True
            self.is_tuning = False
            self.thread = TuningThread(self)
            self.thread.start()
            self.thread.any_signal.connect(self.update_style)
            # self.thread.kill()
        elif self.sender().is_clicked:
            self.is_tuning = True
            self.sender().is_clicked = False

    @Slot(object)
    def update_style(self, command):
        button = command[1]

        if command[0] == "new_note":
            closes_note = Constants.ClosetNote
            closest_note_index = notes.index(closes_note)
            button_note_index = notes.index(button.note)
            if closest_note_index < button_note_index:
                button.setStyleSheet("QPushButton#" + button.name + " { " + button.style_red_up + " }")
                button.setText("")
            if closest_note_index > button_note_index:
                button.setStyleSheet("QPushButton#" + button.name + " { " + button.style_red_down + " }")
                button.setText("")
            if closest_note_index == button_note_index and Constants.NOTE_PITCH > Constants.CURRENT_PITCH + 0.8:
                button.setStyleSheet("QPushButton#" + button.name + " { " + button.style_yellow_up + " }")
                button.setText("")
            elif closest_note_index == button_note_index and Constants.NOTE_PITCH < Constants.CURRENT_PITCH - 0.8:
                button.setStyleSheet("QPushButton#" + button.name + " { " + button.style_yellow_down + " }")
                button.setText("")
            elif closest_note_index == button_note_index:
                button.setStyleSheet("QPushButton#" + button.name + " { " + button.style + " }")
                button.setStyleSheet("QPushButton#" + button.name + " { " + button.style_green + " }")
                button.setText(button.note)
        if command[0] == "stop":
            button.setStyleSheet("QPushButton#" + button.name + " { " + button.style + " }")
            button.setText(button.note)

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


class TuningThread(QThread):

    any_signal = Signal(object)

    def __init__(self, button, parent=None, index=0):
        super(TuningThread, self).__init__(parent)
        self.button = button

    def run(self):
        while True:
            if self.button.is_tuning:
                command = ["stop", self.button]
                self.any_signal.emit(command)
                break
            # self.setEnabled(False)

            better_tuner()
            command = ["new_note", self.button]
            self.any_signal.emit(command)
