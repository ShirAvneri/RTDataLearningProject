from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel

from Project.UI.CommonWidgets.CommonFonts import create_font


class Label(QLabel):
    def __init__(self, x_pos, y_pos, text):
        super(Label, self).__init__()
        self.setGeometry(QRect(x_pos, y_pos, 300, 20))
        self.setFont(create_font(size=12, bold=True))
        self.setText(text)