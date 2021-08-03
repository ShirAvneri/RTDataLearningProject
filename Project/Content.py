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
        self.classical_guitar_tuner()

    def classical_guitar_tuner(self):
        guitar_image_label = QLabel(self)
        guitar_image_label.setObjectName("GuitarImageLabel")
        guitar_image_label.setGeometry(QRect(170, 50, 260, 500))
        guitar_image_label.setStyleSheet("QLabel#GuitarImageLabel { border-image: url(ClassicGuitarTuningPng.png) "
                                         "0 0 0 stretch stretch; }")
        d3 = GuitarTuningButton(self, "D3", 100, 115)
        d3.set_button()
        a2 = GuitarTuningButton(self, "A2", 100, 175)
        a2.set_button()
        e2 = GuitarTuningButton(self, "E2", 100, 235)
        e2.set_button()
        g3 = GuitarTuningButton(self, "G3", 450, 115)
        g3.set_button()
        b3 = GuitarTuningButton(self, "B3", 450, 175)
        b3.set_button()
        e4 = GuitarTuningButton(self, "E4", 450, 235)
        e4.set_button()


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

    def set_button(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font)