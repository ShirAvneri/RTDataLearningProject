from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect

from Project.UI.CommonWidgets.CommonFonts import create_font


class Label(QLabel):
    def __init__(self, x_pos, y_pos, text):
        super(Label, self).__init__()
        self.setGeometry(QRect(x_pos, y_pos, 300, 20))
        self.setFont(create_font(size=12, bold=True))
        self.setText(text)


class CardLabel(QLabel):
    def __init__(self, parent, x_pos, y_pos):
        super(CardLabel, self).__init__(parent)
        self.setGeometry(QRect(x_pos, y_pos, 250, 320))
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(10)
        self.effect.setOffset(2)
        self.setGraphicsEffect(self.effect)
        self.setStyleSheet("background-color: white; border: 1px solid black; border-radius: 10px")