from PySide6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QWidget, QLabel
from Project.UI.BaseComponent import BaseGuiComponent
from Project.UI.CommonWidgets.CommonFonts import create_font


class SideMenu(QWidget, BaseGuiComponent):
    def __init__(self):
        super(SideMenu, self).__init__()
        self.name = "SideMenu"
        self.style = "background-color: #ffffff; border-top-left-radius: 10px; border-bottom-left-radius: 10px;"
        self.setGeometry(QRect(600, 50, 300, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")
        # Setting tool-box title:
        self.toolBoxLabel = QLabel(self)
        self.toolBoxLabel.setGeometry(QRect(10, 20, 150, 30))
        self.toolBoxLabel.setFont(create_font(size=20, bold=True))
        self.toolBoxLabel.setText("TOOL KIT")
