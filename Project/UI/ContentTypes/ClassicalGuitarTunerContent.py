from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QLabel, QFrame
from Project.UI.Content import Content
from Project.UI.ContentTypes.Common import GuitarTunerButton


class ClassicalGuitarTunerContent(Content):
    def __init__(self):
        super(ClassicalGuitarTunerContent, self).__init__()
        self.notes = ["E4", "B3", "G3", "D3", "A2", "E2"]
        self.notes_buttons = []
        guitar_image = QLabel(self)
        guitar_image.setObjectName("GuitarImageLabel")
        guitar_image.setGeometry(QRect(170, 50, 260, 500))
        guitar_image.setStyleSheet("QLabel#GuitarImageLabel { "
                                   "border-image: url(./UI/Images/ClassicGuitarTuningPng.png) 0 0 0 stretch stretch; }")
        self.label_your_note = QLabel(self)
        self.label_your_note.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.label_your_note.setText("label_your_note")
        self.label_your_note.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.label_your_note.setGeometry(QRect(100, 10, 100, 30));

        self.label_position = QLabel(self)
        self.label_position.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.label_position.setText("up\down")
        self.label_position.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        self.init_notes()

    def init_notes(self):
        string1 = GuitarTunerButton( self.notes[0], "1", 450, 235)
        self.notes_buttons.append(string1)

        string2 = GuitarTunerButton(self.notes[1], "2", 450, 175)
        self.notes_buttons.append(string2)

        string3 = GuitarTunerButton( self.notes[2], "3", 450, 115)
        self.notes_buttons.append(string3)

        string4 = GuitarTunerButton( self.notes[3], "4", 100, 115)
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
