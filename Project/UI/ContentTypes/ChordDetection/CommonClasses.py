from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton

from Project.ChordRecording import main_recording
from Project.UI.CommonWidgets.WidgetsFactory import font_factory


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
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + "Recording  Button" + " { " + self.style + " }")
        self.setText("RECORD")
        self.setFont(font_factory(size=14))
        self.clicked.connect(main_recording)


class ChordAnalyzingButton(QPushButton):
    def __init__(self, x_pos, y_pos):
        super(ChordAnalyzingButton, self).__init__()
        self.setObjectName("Analyzing Button")
        self.x = x_pos
        self.y = y_pos
        self.path = "b"
        self.style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                     "border-radius: 25px; "
        self.set_button()

    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        self.setStyleSheet("QPushButton#" + "Recording  Button" + " { " + self.style + " }")
        self.setText("Analyze")
        self.setFont(font_factory(size=14))

