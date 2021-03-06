from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QPushButton, QButtonGroup, QRadioButton, QGraphicsDropShadowEffect, QFileDialog
from Project.UI.CommonWidgets.CommonFonts import create_font


class GuitarButton(QPushButton):
    def __init__(self, parent, click_signal, x_pos, y_pos, icon_path=None):
        super(GuitarButton, self).__init__(parent)
        self.click_signal = click_signal
        self.style = "background-color: #f5f5f5; background-radius: 10px; border-radius: 10px;"
        self.setStyleSheet(self.style)
        self.setGeometry(QRect(x_pos, y_pos, 80, 80))
        if icon_path is not None:
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(80, 80))
        self.clicked.connect(self.click_event)

    def click_event(self):
        self.parent().notify(self.click_signal)


class RadioButtonsGroup(QButtonGroup):
    def __init__(self, invoke_on_click, click_signal, x_pos, y_pos, buttons_names):
        super(RadioButtonsGroup, self).__init__()
        self.invoke_on_click = invoke_on_click
        self.click_signal = click_signal
        self.buttons_names = buttons_names
        self.x = x_pos
        self.y = y_pos
        self.margin = 20

    def set_buttons(self):
        for i, text in enumerate(self.buttons_names):
            radio_button = QRadioButton(self.parent())
            radio_button.setGeometry(QRect(self.x, self.y + i * self.margin, 300, 20))
            radio_button.setFont(create_font(size=10))
            radio_button.setText(text)
            radio_button.setStyleSheet("color: #393939;")
            self.addButton(radio_button, i)
        self.buttonClicked.connect(self.button_clicked)
        self.init_selected_button()

    def init_selected_button(self):
        self.buttons()[0].setChecked(True)

    def button_clicked(self, button: QRadioButton):
        if self.invoke_on_click is not None:
            self.invoke_on_click(self.click_signal, button.text())


class StartStopButton(QPushButton):
    def __init__(self, start_function, stop_function, start_text="START", stop_text="STOP"):
        super(StartStopButton, self).__init__()
        self.is_start = True
        self.start_function = start_function
        self.stop_function = stop_function
        self.start_text = start_text
        self.stop_text = stop_text
        self.start_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                           "background-color: #00a215; border-radius: 55px;"
        self.stop_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                          "background-color: #972c2c; border-radius: 55px;"
        self.clicked.connect(self.button_clicked)

    def init_style(self, button_name: str, x_pos: int, y_pos: int):
        self.setObjectName(button_name)
        self.setGeometry(QRect(x_pos, y_pos, 110, 110))
        self.setText(self.start_text)
        self.setStyleSheet(self.start_style)
        self.setFont(create_font(size=16, bold=True))
        effect = QGraphicsDropShadowEffect(self)
        effect.setColor(QColor(117, 117, 117))
        effect.setOffset(0)
        effect.setBlurRadius(15)
        self.setGraphicsEffect(effect)

    def button_clicked(self):
        if self.is_start:
            self.setText(self.stop_text)
            self.setStyleSheet(self.stop_style)
            self.start_function()
            self.is_start = False
        else:
            self.setText(self.start_text)
            self.setStyleSheet(self.start_style)
            self.stop_function()
            self.is_start = True


class FilePickerButton(QPushButton):
    def __init__(self):
        super(FilePickerButton, self).__init__()
        self.start_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                           "background-color: #00a215; border-radius: 50px;"
        self.stop_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                          "background-color: #972c2c; border-radius: 50px;"
        self.clicked.connect(self.button_clicked)
        self.path = ""

    def init_style(self, button_name: str, x_pos: int, y_pos: int):
        self.setObjectName(button_name)
        self.setGeometry(QRect(x_pos, y_pos, 100, 100))
        self.setText("Upload")
        self.setStyleSheet(self.start_style)
        self.setFont(create_font(size=16, bold=True))
        effect = QGraphicsDropShadowEffect(self)
        effect.setColor(QColor(117, 117, 117))
        effect.setOffset(0)
        effect.setBlurRadius(15)
        self.setGraphicsEffect(effect)

    def button_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, "open a file", "C://")
        self.path = file_name
