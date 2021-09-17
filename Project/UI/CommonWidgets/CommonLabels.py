from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from Project.UI.CommonWidgets.CommonFonts import create_font


class Label(QLabel):
    def __init__(self, parent, x_pos, y_pos, text, is_light=False):
        super(Label, self).__init__(parent)
        self.setGeometry(QRect(x_pos, y_pos, 300, 20))
        if is_light:
            self.setStyleSheet("color: rgba(85, 85, 85, 0.5)")
        self.setFont(create_font(size=10, bold=True))
        self.setText(text)


class CardLabel(QLabel):
    def __init__(self, parent, x_pos, y_pos, image_url):
        super(CardLabel, self).__init__(parent)
        self.setGeometry(QRect(x_pos, y_pos, 250, 320))
        self.setStyleSheet("background-color: #fcfcfc; border-radius: 10px;")
        self.effect = QGraphicsDropShadowEffect()
        self.setGraphicsEffect(self.effect)
        self.effect.setBlurRadius(5)
        self.effect.setOffset(2)
        self.image = QLabel(self)
        self.image.setGeometry(QRect(151, 0, 100, 320))
        self.image.setStyleSheet(f"border-image: url({image_url}) 0 0 0 stretch stretch;")

