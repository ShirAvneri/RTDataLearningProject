from PySide6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget, QPushButton


class TopBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "TopBar"
        self.style = "background-color: rgb(57, 57, 57); border-bottom-right-radius: 10px; " \
                     "border-bottom-left-radius: 10px;"
        self.setGeometry(QRect(0, 0, 900, 50))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")

        self.buttons_types = ["some_button1", "some_button2", "some_button3", "some_button4", "some_button5",
                              "some_button6", "some_button7"]
        self.buttons_style = "color: white; text-align: left; background-color: rgb(57, 57, 57);  border-radius: 0px; "\
                             "border-right-style: outset; border-right-width: 1px; border-right-color: rgb(97, 97, 97);"
        self.buttons_x = 20
        self.buttons_margin = 120
        self.buttons_list = {}
        self.set_buttons()

    def set_buttons(self):
        for i, text in enumerate(self.buttons_types):
            button = QPushButton(self)
            button.setGeometry(QRect(self.buttons_x + self.buttons_margin * i, 0, 100, 49))
            button.setStyleSheet(self.buttons_style)
            button.setText(text)
            self.buttons_list[text] = button
