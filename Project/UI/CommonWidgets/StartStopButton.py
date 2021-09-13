from PySide6.QtCore import QRect
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from Project.UI.CommonWidgets.FontFactory import create_font


class StartStopButton(QPushButton):
    def __init__(self, start_function, stop_function):
        super(StartStopButton, self).__init__()
        self.is_start = True
        self.start_function = start_function
        self.stop_function = stop_function
        self.start_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                           "background-color: #00a215; border-radius: 50px;"
        self.stop_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                          "background-color: #972c2c; border-radius: 50px;"
        self.clicked.connect(self.button_clicked)

    def init_style(self, button_name: str, x_pos: int, y_pos: int):
        self.setObjectName(button_name)
        self.setGeometry(QRect(x_pos, y_pos, 100, 100))
        self.setText("START")
        self.setStyleSheet(self.start_style)
        self.setFont(create_font(size=16, bold=True))
        effect = QGraphicsDropShadowEffect(self)
        effect.setColor(QColor(117, 117, 117))
        effect.setOffset(0)
        effect.setBlurRadius(15)
        self.setGraphicsEffect(effect)

    def button_clicked(self):
        if self.is_start:
            self.setText("STOP")
            self.setStyleSheet(self.stop_style)
            self.start_function()
            self.is_start = False
        else:
            self.setText("START")
            self.setStyleSheet(self.start_style)
            self.stop_function()
            self.is_start = True


