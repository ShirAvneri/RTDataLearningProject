from PySide6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget
from Project.UI.BaseComponent import BaseGuiComponent


class Content(QWidget, BaseGuiComponent):
    def __init__(self, full_screen=False):
        super(Content, self).__init__()
        self.name = "Content"
        self.style = ""  # Will maybe needed in the future
        if full_screen:
            self.setGeometry(QRect(0, 50, 900, 550))
        else:
            self.setGeometry(QRect(0, 50, 600, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")