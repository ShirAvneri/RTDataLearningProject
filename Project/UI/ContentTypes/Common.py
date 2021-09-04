from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton


class GuitarTunerButton(QPushButton):
    def __init__(self, parent, note, x_pos, y_pos):
        super().__init__(parent)
        self.note = note
        self.name = note + "_note"
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.set_button()

    def set_button(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font)

    def change_note(self, note):
        self.note = note
        self.name = note + "_note"
        self.setObjectName(self.name)
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
