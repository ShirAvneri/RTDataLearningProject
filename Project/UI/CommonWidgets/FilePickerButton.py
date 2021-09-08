from PySide6.QtCore import QRect, QDir
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QFileDialog


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
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(True)
        self.setFont(font)
        effect = QGraphicsDropShadowEffect(self)
        effect.setColor(QColor(117, 117, 117))
        effect.setOffset(0)
        effect.setBlurRadius(15)
        self.setGraphicsEffect(effect)

    def button_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, "open a file", "C://")
        self.path = file_name


