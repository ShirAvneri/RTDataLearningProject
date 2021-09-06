from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton

from Project.Recording import main_recording
from Project.Tuner import main_tuner


class GuitarTunerButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(GuitarTunerButton, self).__init__()
        self.note = note
        self.name = "string" + string_num
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
        self.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.parent().label_your_note.setText("HADAR")
        print("in buttin clicked")
        print(type(self.parent()))
        print(self.parent().label_your_note.text())
        main_tuner(self.parent().label_your_note)

    def change_note(self, note, string_num):
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)


class RecordingButton(QPushButton):
    def __init__(self, x_pos, y_pos):
        super(RecordingButton, self).__init__()
        self.setObjectName("Recording Button")
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
        self.setStyleSheet("QPushButton#" + "Recording  Button" + " { " + self.style + " }")
        self.setText("RECORD")
        self.setFont(font)
        self.clicked.connect(main_recording())


class SingleChordRecordingButton(QPushButton):
    def __init__(self, x_pos, y_pos):
        super(SingleChordRecordingButton, self).__init__()
        self.setObjectName("Recording")
        self.x = x_pos
        self.y = y_pos
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.set_button()

    def set_button(self):
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + "Recording  Button" + " { " + self.style + " }")
        self.setText("Record Chord")
        self.setFont(font)
