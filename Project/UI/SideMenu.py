from PySide6 import QtCore
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton, QButtonGroup
import json


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
        # Setting everything else:
        self.chooseInstrumentLabel = SideMenuLabel(10, 60, "CHOOSE AN INSTRUMENT")
        self.chooseInstrumentLabel.setParent(self)
        self.classicalBtn = SideMenuButton(20, 85)
        self.classicalBtn.set_icon("./UI/Images/ClassicGuitarPngIcon.png")
        self.classicalBtn.setParent(self)
        self.acousticBtn = SideMenuButton(110, 85)
        self.acousticBtn.set_icon("./UI/Images/AcousticGuitarPngIcon.png")
        self.acousticBtn.setParent(self)
        self.electricBtn = SideMenuButton(200, 85)
        self.electricBtn.set_icon("./UI/Images/ElectricGuitarPngIcon.png")
        self.electricBtn.setParent(self)
        self.chooseTuningLabel = SideMenuLabel(10, 180, "CHOOSE TUNING")
        self.chooseTuningLabel.setParent(self)
        self.radio_buttons = SideMenuRadioButtons(20, 205)
        self.radio_buttons.setParent(self)
        self.radio_buttons.set_buttons()

    def tuning_changed_event(self, notes):
        self.parent().change_tuning(notes)


class SideMenuButton(QPushButton):
    def __init__(self, x_pos, y_pos):
        super(SideMenuButton, self).__init__()
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
    def __init__(self, x_pos, y_pos, text):
        super(SideMenuLabel, self).__init__()
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        font.setBold(True)
        self.setGeometry(QRect(x_pos, y_pos, 150, 20))
        self.setFont(font)
        self.setText(text)


class SideMenuRadioButtons(QButtonGroup):
    def __init__(self, x_pos, y_pos):
        super(SideMenuRadioButtons, self).__init__()
        self.tuning_list = ["Standard", "Drop D", "Drop C", "Drop C#", "Drop B", "Drop A", "DADGAD", "Half Step Down",
                            "Full Step Down", "Half Step Up", "Open C", "Open D", "Open E", "Open F", "Open G",
                            "Open A"]
        self.x = x_pos
        self.y = y_pos
        self.margin = 20

    def set_buttons(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        for i, text in enumerate(self.tuning_list):
            radio_button = QRadioButton()
            radio_button.setGeometry(QRect(self.x, self.y + i * self.margin, 150, 20))
            radio_button.setFont(font)
            radio_button.setText(text)
            radio_button.setParent(self.parent())
            self.addButton(radio_button, i)
        self.buttonClicked.connect(self.tuning_changed)

    def tuning_changed(self, button: QRadioButton):
        selected_tuning = self.tuning_list[self.id(button)]
        f = open('./UI/TuningNotes.json', )
        tunings = json.load(f)
        self.parent().tuning_changed_event(tunings[selected_tuning])
