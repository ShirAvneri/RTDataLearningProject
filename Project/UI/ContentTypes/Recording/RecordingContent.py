from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel
from Project.UI.Content import Content
from Project.UI.ContentTypes.Recording.CommonClasses import RecordingButton


class RecordingContent(Content):
    def __init__(self):
        super(RecordingContent, self).__init__()
        self.notes_buttons = []
        recording_image = QLabel(self)
        recording_image.setObjectName("Recording")
        recording_image.setGeometry(QRect(500, 50, 260, 500))
        recording_image.setStyleSheet(
            "QLabel#Recording { ""border-image: url(./UI/Images/Recording.png) 0 0 0 stretch stretch; }")
        self.make_button()

    def make_button(self):
        string1 = RecordingButton(450, 235)
        string1.clicked.connect(self.button_clicked)
        self.notes_buttons.append(string1)
        for button in self.notes_buttons:
            button.setParent(self)

    def button_clicked(self):
        pass
