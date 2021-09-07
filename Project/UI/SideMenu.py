from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from Project.UI.SideMenuTypes.CommonClasses import *


class SideMenu(QWidget):
    def __init__(self):
        super(SideMenu, self).__init__()
        self.name = "SideMenu"
        self.style = "background-color: #ffffff; border-top-left-radius: 10px; border-bottom-left-radius: 10px;"
        self.setGeometry(QRect(600, 50, 300, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")
        # Setting tool-box title:
        title_font = QFont()
        title_font.setFamilies([u"Calibri"])
        title_font.setPointSize(24)
        title_font.setBold(True)
        self.toolBoxLabel = QLabel(self)
        self.toolBoxLabel.setGeometry(QRect(10, 20, 150, 30))
        self.toolBoxLabel.setFont(title_font)
        self.toolBoxLabel.setText("Tool Box")
        self.toolBoxLabel.setParent(self)
