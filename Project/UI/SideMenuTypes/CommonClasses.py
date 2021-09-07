import json

from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QPushButton, QLabel, QButtonGroup, QRadioButton


class SideMenuGuitarButton(QPushButton):
    def __init__(self, guitar_type, x_pos, y_pos):
        super(SideMenuGuitarButton, self).__init__()
        self.guitar_type = guitar_type
        self.style = "background-color: #f5f5f5; background-radius: 10px; border-radius: 10px;"
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet(self.style)
        self.setGeometry(QRect(x_pos, y_pos, 80, 80))
        self.clicked.connect(self.change_guitar)

    def set_icon(self, path):
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(80, 80))

    def change_guitar(self):
        self.parent().guitar_change_event(self.guitar_type)


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

    def init_selected_button(self):
        self.buttons()[0].setChecked(True)

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
        self.buttonClicked.connect(self.change_tuning)
        self.init_selected_button()

    def change_tuning(self, button: QRadioButton):
        selected_tuning = self.tuning_list[self.id(button)]
        f = open('./UI/TuningNotes.json', )
        tunings = json.load(f)
        self.parent().tuning_change_event(tunings[selected_tuning])
