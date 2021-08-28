from PySide6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QPushButton


class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "Content"
        self.style = ""
        self.setGeometry(QRect(0, 50, 600, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")


class ClassicalGuitarTuner(Content):
    def __init__(self, parent):
        super().__init__(parent)
        self.notes = ["E4", "B3", "G3", "D3", "A2", "E2"]
        self.notes_buttons = []
        guitar_image = QLabel(self)
        guitar_image.setObjectName("GuitarImageLabel")
        guitar_image.setGeometry(QRect(170, 50, 260, 500))
        guitar_image.setStyleSheet("QLabel#GuitarImageLabel { border-image: url(ClassicGuitarTuningPng.png) "
                                   "0 0 0 stretch stretch; }")
        self.init_notes()

    def init_notes(self):
        string1 = GuitarTuningButton(self, self.notes[0], 450, 235)
        self.notes_buttons.append(string1)
        string2 = GuitarTuningButton(self, self.notes[1], 450, 175)
        self.notes_buttons.append(string2)
        string3 = GuitarTuningButton(self, self.notes[2], 450, 115)
        self.notes_buttons.append(string3)
        string4 = GuitarTuningButton(self, self.notes[3], 100, 115)
        self.notes_buttons.append(string4)
        string5 = GuitarTuningButton(self, self.notes[4], 100, 175)
        self.notes_buttons.append(string5)
        string6 = GuitarTuningButton(self, self.notes[5], 100, 235)
        self.notes_buttons.append(string6)


    def change_notes(self, notes: []):
        for i, _ in enumerate(self.notes_buttons):
            self.notes[i] = notes[i]
            self.notes_buttons[i].change_note(notes[i])


class GuitarTuningButton(QPushButton):
    def __init__(self, parent, note, x_pos, y_pos):
        super().__init__(parent)
        self.note = note
        self.name = note + "_note"
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.set_button()

    def set_button(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font)

    def change_note(self, note):
        self.note = note
        self.name = note + "_note"
        self.setObjectName(self.name)
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
