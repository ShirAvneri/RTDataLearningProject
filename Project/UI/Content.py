from PySide6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget


class Content(QWidget):
    def __init__(self):
        super(Content, self).__init__()
        self.name = "Content"
        self.style = ""  # Will maybe needed in the future
        self.setGeometry(QRect(0, 50, 600, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")