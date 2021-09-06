from PySide6 import QtCore
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton
from Project.Constants import *


class TopBar(QWidget):
    def __init__(self):
        super(TopBar, self).__init__()
        self.name = "TopBar"
        self.style = "background-color: #393939; border-bottom-right-radius: 10px; " \
                     "border-bottom-left-radius: 10px;"
        self.setGeometry(QRect(0, 0, 900, 50))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")

        self.buttons_types = [GUITAR_TUNING, RECORDING, CHORD_DETECTION]
        self.buttons_icons = ["./UI/Images/TopBarIcons/GuitarTuning.png", "./UI/Images/TopBarIcons/Recording.png",
                              "./UI/Images/TopBarIcons/ChordDetection.png"]
        self.buttons_style = "color: white; text-align: center; background-color: #393939; border-radius: 0px;" \
                             "border-right-style: outset; border-right-width: 1px; border-right-color: #616161;"
        self.buttons_x = 20
        self.buttons_margin = 140
        self.buttons_list = {}
        self.set_buttons()

    def set_buttons(self):
        for i, text in enumerate(self.buttons_types):
            button = QPushButton(self)
            button.setGeometry(QRect(self.buttons_x + self.buttons_margin * i, 0, 135, 49))
            button.setStyleSheet(self.buttons_style)
            button.setText(text)
            button.setIcon(QIcon(self.buttons_icons[i]))
            button.setIconSize(QSize(27, 27))
            button.clicked.connect(self.button_clicked)
            self.buttons_list[text] = button

    def button_clicked(self):
        print(self.sender().text())
        self.parent().change_content(self.sender().text())
