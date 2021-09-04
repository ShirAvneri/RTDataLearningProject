from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel, QPushButton
from Project.UI.Content import Content
from Project.UI.ContentTypes.Common import GuitarTunerButton


class ClassicalGuitarTunerContent(Content):
    def __init__(self, parent):
        super().__init__(parent)
        self.notes = ["E4", "B3", "G3", "D3", "A2", "E2"]
        self.notes_buttons = []
        guitar_image = QLabel(self)
        guitar_image.setObjectName("GuitarImageLabel")
        guitar_image.setGeometry(QRect(170, 50, 260, 500))
        guitar_image.setStyleSheet("QLabel#GuitarImageLabel { "
                                   "border-image: url(./UI/Images/ClassicGuitarTuningPng.png) 0 0 0 stretch stretch; }")
        self.init_notes()

    def init_notes(self):
        string1 = GuitarTunerButton(self, self.notes[0], 450, 235)
        self.notes_buttons.append(string1)
        string2 = GuitarTunerButton(self, self.notes[1], 450, 175)
        self.notes_buttons.append(string2)
        string3 = GuitarTunerButton(self, self.notes[2], 450, 115)
        self.notes_buttons.append(string3)
        string4 = GuitarTunerButton(self, self.notes[3], 100, 115)
        self.notes_buttons.append(string4)
        string5 = GuitarTunerButton(self, self.notes[4], 100, 175)
        self.notes_buttons.append(string5)
        string6 = GuitarTunerButton(self, self.notes[5], 100, 235)
        self.notes_buttons.append(string6)

    def change_notes(self, notes: []):
        for i, _ in enumerate(self.notes_buttons):
            self.notes[i] = notes[i]
            self.notes_buttons[i].change_note(notes[i])


