from PySide6 import QtCore
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton, QButtonGroup
import json


class SideMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = parent
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

        # Setting everything else:
        self.chooseInstrumentLabel = SideMenuLabel(self, 10, 60, "CHOOSE AN INSTRUMENT")
        self.classicalBtn = SideMenuButton(self, 20, 85)
        self.classicalBtn.set_icon("./UI/Images/ClassicGuitarPngIcon.png")
        self.acousticBtn = SideMenuButton(self, 110, 85)
        self.acousticBtn.set_icon("./UI/Images/AcousticGuitarPngIcon.png")
        self.electricBtn = SideMenuButton(self, 200, 85)
        self.electricBtn.set_icon("./UI/Images/ElectricGuitarPngIcon.png")
        self.chooseTuningLabel = SideMenuLabel(self, 10, 180, "CHOOSE TUNING")
        self.radio_buttons = SideMenuRadioButtons(self, 20, 205)
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
        self.tuning_list = ["Standard", "Drop D", "Drop C", "Drop C#", "Drop B", "Drop A", "DADGAD", "Half Step Down",
                            "Full Step Down", "Half Step Up", "Open C", "Open D", "Open E", "Open F", "Open G",
                            "Open A"]
        self.parent = parent
        self.x = x_pos
        self.y = y_pos
        self.margin = 20
        self.buttons_list = {}
        self.buttons_group = QButtonGroup(parent)

    def set_buttons(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        for i, text in enumerate(self.tuning_list):
            radio_button = QRadioButton(self.parent)
            radio_button.setGeometry(QRect(self.x, self.y + i * self.margin, 150, 20))
            radio_button.setFont(font)
            radio_button.setText(text)
            self.buttons_list[text] = radio_button
            self.buttons_group.addButton(radio_button, i)
        self.buttons_group.buttonClicked.connect(self.change_notes)

    def change_notes(self, button: QRadioButton):
        selected_tuning = self.tuning_list[self.buttons_group.id(button)]
        f = open('./UI/TuningNotes.json',)
        tunings = json.load(f)
        print(tunings[selected_tuning])
        self.parent.main_layout.change_tuning_event(tunings[selected_tuning])
