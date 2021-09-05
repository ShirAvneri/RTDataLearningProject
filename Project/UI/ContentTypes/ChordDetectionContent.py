from PySide6.QtCore import QRect
from PySide6.QtWidgets import QLabel
from Project.UI.Content import Content
from Project.UI.ContentTypes.Common import GuitarTunerButton


class ChordDetectionContent(Content):
    def __init__(self):
        super(ChordDetectionContent, self).__init__()
        self.notes = ["123", "B3", "G3", "D3", "A2", "E2"]
        self.notes_buttons = []
        guitar_image = QLabel(self)
        guitar_image.setObjectName("GuitarImageLabel")
        guitar_image.setGeometry(QRect(500, 50, 260, 500))
        guitar_image.setStyleSheet("QLabel#GuitarImageLabel { "
                                   "border-image: url(./UI/Images/ClassicGuitarTuningPng.png) 0 0 0 stretch stretch; }")
        self.init_notes()

    def init_notes(self):
        string1 = GuitarTunerButton(self.notes[0], "1", 450, 235)
        self.notes_buttons.append(string1)
        string2 = GuitarTunerButton(self.notes[1], "2", 450, 175)
        self.notes_buttons.append(string2)
        string3 = GuitarTunerButton(self.notes[2], "3", 450, 115)
        self.notes_buttons.append(string3)
        string4 = GuitarTunerButton(self.notes[3], "4", 100, 115)
        self.notes_buttons.append(string4)
        string5 = GuitarTunerButton(self.notes[4], "5", 100, 175)
        self.notes_buttons.append(string5)
        string6 = GuitarTunerButton(self.notes[5], "6", 100, 235)
        self.notes_buttons.append(string6)
        for button in self.notes_buttons:
            button.setParent(self)

    def change_notes(self, notes: []):
        for i, _ in enumerate(self.notes_buttons):
            self.notes[i] = notes[i]
            self.notes_buttons[i].change_note(notes[i], str(i+1))
