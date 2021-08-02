from PySide6 import QtCore
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton


class SideMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "SideMenu"
        self.style = "background-color: #ffffff; border-top-left-radius: 10px; border-bottom-left-radius: 10px;"
        self.setGeometry(QRect(600, 50, 300, 550))
        self.setObjectName(self.name)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("QWidget#" + self.name + " { " + self.style + " }")

        # Setting tool-box title:
        title_font = QFont()
        title_font.setFamilies([u"Calibri"])
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.toolBoxLabel = QLabel(self)
        self.toolBoxLabel.setGeometry(QRect(10, 20, 100, 30))
        self.toolBoxLabel.setFont(title_font)
        self.toolBoxLabel.setText("Tool Box")

        # Setting everything else:
        self.chooseInstrumentLabel = SideMenuLabel(self, 10, 60, "CHOOSE AN INSTRUMENT")
        self.classicalBtn = SideMenuButton(self, 20, 90)
        self.classicalBtn.set_icon("Images\\ClassicGuitarPngIcon.png")
        self.acousticBtn = SideMenuButton(self, 110, 90)
        self.acousticBtn.setText("Acoustic")  # Needs to be changed to icon
        self.electricBtn = SideMenuButton(self, 200, 90)
        self.electricBtn.set_icon("Images\\ElectricGuitarPngIcon.png")
        self.chooseTuningLabel = SideMenuLabel(self, 10, 190, "CHOOSE TUNING")
        self.radio_buttons = SideMenuRadioButtons(self, 20, 220)
        self.radio_buttons.set_buttons()


class SideMenuButton(QPushButton):
    def __init__(self, parent, x_pos, y_pos):
        super().__init__(parent)
        self.style = "background-color: #f5f5f5; background-radius: 10px; border-radius: 10px;"
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet(self.style)
        self.setGeometry(QRect(x_pos, y_pos, 80, 80))

    def set_icon(self, path):
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(80, 80))


class SideMenuLabel(QLabel):
    def __init__(self, parent, x_pos, y_pos, text):
        super().__init__(parent)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        font.setBold(True)
        self.setGeometry(QRect(x_pos, y_pos, 150, 20))
        self.setFont(font)
        self.setText(text)


class SideMenuRadioButtons:
    def __init__(self, parent, x_pos, y_pos):
        self.tuning_list = ["Regular", "Drop D", "Double drop D", "DADGAD", "Open D", "Open E", "Open G", "Open A",
                            "Open C", "Open C6"]
        self.parent = parent
        self.x = x_pos
        self.y = y_pos
        self.margin = 20
        self.buttons_list = {}

    def set_buttons(self):
        for i, text in enumerate(self.tuning_list):
            radio_button = QRadioButton(self.parent)
            radio_button.setGeometry(QRect(self.x, self.y + i * self.margin, 150, 20))
            radio_button.setText(text)
            self.buttons_list[text] = radio_button
