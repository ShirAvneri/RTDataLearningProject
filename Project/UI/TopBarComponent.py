import os

from PySide6 import QtCore
from PySide6.QtCore import QSize, QRect
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton
from Project.Constants import IMAGES_PATH, TOP_BAR_FUNCTIONALITY
from Project.UI.BaseComponent import BaseGuiComponent

# TO DO:
# Disable buttons when a content thread is running


class TopBar(QWidget, BaseGuiComponent):
    def __init__(self):
        super(TopBar, self).__init__()
        self.name = "TopBar"
        self.style = "background-color: #393939; border-bottom-right-radius: 10px; " \
                     "border-bottom-left-radius: 10px;"
        self.setGeometry(QRect(0, 0, 900, 50))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")
        self.icons_path = os.path.join(IMAGES_PATH, 'TopBarIcons')
        self.icons_names = ["GuitarTuning.png", "Recording.png", "ChordDetection.png", "Metronome.png",
                            "AudioAnalysis.png", "PitchTraining.png"]
        self.buttons_style = "color: white; text-align: center; background-color: #393939; border-radius: 0px;" \
                             "border-right-style: outset; border-right-width: 1px; border-right-color: #616161;"
        self.buttons_x = 20
        self.buttons_margin = 140
        self.buttons_list = {}
        self.set_buttons()

    def set_buttons(self):
        for key, val in TOP_BAR_FUNCTIONALITY.items():
            i = int(val.value)
            button = QPushButton(self)
            button.setGeometry(QRect(self.buttons_x + self.buttons_margin * i, 0, 135, 49))
            button.setStyleSheet(self.buttons_style)
            button.setText(key)
            button.setIcon(QIcon(f"{self.icons_path}/{self.icons_names[i]}"))
            button.setIconSize(QSize(27, 27))
            button.clicked.connect(self.button_clicked)
            self.buttons_list[i] = button

    def button_clicked(self):
        key = self.sender().text()
        self.mediator.notify(TOP_BAR_FUNCTIONALITY[key])
