from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton

from Project.UI.CommonWidgets.WidgetsFactory import font_factory


class MusicButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(MusicButton, self).__init__()
        self.Flag = 0
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.is_on="0"

        self.clicked.connect(self.start_music)
        self.set_button()


    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font_factory(size=14))

    def start_music(self):
        print("start tuner")
        #self.style = "background-color: red; "
        if self.is_on:
            self.is_on = 0
            if self.sender().text() in self.parent().notes:
                self.parent().current_notes = "0"
            elif self.sender().text() in self.parent().finger_pick:
                self.parent().current_fp = "0"
            elif self.sender().text() in self.parent().type:
                self.parent().current_type = "0"
        else:
            self.is_on = 1
            if self.sender().text() in self.parent().notes:
                self.parent().current_notes = self.sender().text()
            elif self.sender().text() in self.parent().finger_pick:
                self.parent().current_fp = self.sender().text()
            elif self.sender().text() in self.parent().type:
                self.parent().current_type = self.sender().text()
        print(self.sender().text())


