from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QFormLayout, QGroupBox, QLabel, QScrollArea
import sys
from PySide6 import QtGui

class ChordWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "chord area"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = ""

        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()







