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
        font.setPointSize(12)
        font.setBold(True)
        self.setGeometry(QRect(x_pos, y_pos, 150, 20))
        self.setFont(font)
        self.setText(text)


class SideMenuRadioButtons(QButtonGroup):
    def __init__(self, x_pos, y_pos, clicked_invoke_function, buttons_texts):
        super(SideMenuRadioButtons, self).__init__()
        self.clicked_invoke_function = clicked_invoke_function
        self.buttons_texts = buttons_texts
        self.x = x_pos
        self.y = y_pos
        self.margin = 20

    def init_selected_button(self):
        self.buttons()[0].setChecked(True)

    def set_buttons(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        for i, text in enumerate(self.buttons_texts):
            radio_button = QRadioButton()
            radio_button.setGeometry(QRect(self.x, self.y + i * self.margin, 150, 20))
            radio_button.setFont(font)
            radio_button.setText(text)
            radio_button.setParent(self.parent())
            self.addButton(radio_button, i)
        self.buttonClicked.connect(self.button_clicked)
        self.init_selected_button()

    def button_clicked(self, button: QRadioButton):
        self.clicked_invoke_function(button.text())
