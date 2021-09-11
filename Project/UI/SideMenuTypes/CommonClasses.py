from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QLabel, QButtonGroup, QRadioButton
from Project.UI.CommonWidgets.WidgetsFactory import font_factory


class SideMenuGuitarButton(QPushButton):
    def __init__(self, click_signal, x_pos, y_pos):
        super(SideMenuGuitarButton, self).__init__()
        self.click_signal = click_signal
        self.style = "background-color: #f5f5f5; background-radius: 10px; border-radius: 10px;"
        self.setStyleSheet(self.style)
        self.setGeometry(QRect(x_pos, y_pos, 80, 80))
        self.clicked.connect(self.click_event)

    def set_icon(self, path):
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(80, 80))

    def click_event(self):
        self.parent().notify(self.click_signal)


class SideMenuLabel(QLabel):
    def __init__(self, x_pos, y_pos, text):
        super(SideMenuLabel, self).__init__()
        self.setGeometry(QRect(x_pos, y_pos, 300, 20))
        self.setFont(font_factory(size=12, bold=True))
        self.setText(text)


class SideMenuRadioButtons(QButtonGroup):
    def __init__(self, invoke_on_click, click_signal, x_pos, y_pos, buttons_names):
        super(SideMenuRadioButtons, self).__init__()
        self.invoke_on_click = invoke_on_click
        self.click_signal = click_signal
        self.buttons_names = buttons_names
        self.x = x_pos
        self.y = y_pos
        self.margin = 20

    def init_selected_button(self):
        self.buttons()[0].setChecked(True)

    def set_buttons(self):
        for i, text in enumerate(self.buttons_names):
            radio_button = QRadioButton()
            radio_button.setGeometry(QRect(self.x, self.y + i * self.margin, 300, 20))
            radio_button.setFont(font_factory(size=12))
            radio_button.setText(text)
            radio_button.setParent(self.parent())
            self.addButton(radio_button, i)
        self.buttonClicked.connect(self.button_clicked)
        self.init_selected_button()

    def button_clicked(self, button: QRadioButton):
        self.invoke_on_click(self.click_signal, button.text())
