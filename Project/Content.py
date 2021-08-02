from PySide6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget, QLabel


class Content(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "Content"
        self.style = ""
        self.setGeometry(QRect(0, 50, 600, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")
        self.guitar_tuner_content()

    def guitar_tuner_content(self):
        guitar_image_label = QLabel(self)
        guitar_image_label.setObjectName("GuitarImageLabel")
        guitar_image_label.setGeometry(QRect(120, 100, 300, 500))
        guitar_image_label.setStyleSheet("QLabel#GuitarImageLabel { border-image: url(ClassicGuitarTuningPng.png) "
                                         "0 0 0 stretch stretch; }")
