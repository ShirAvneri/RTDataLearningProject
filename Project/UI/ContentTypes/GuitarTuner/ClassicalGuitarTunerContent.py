from PySide6.QtCore import QRect

from Project.UI.ContentTypes.GuitarTuner.CommonClasses import GuitarTunerButton
from Project.UI.ContentTypes.GuitarTuner.GuitarTunerContent import GuitarTunerContent


class ClassicalGuitarTunerContent(GuitarTunerContent):
    def __init__(self):
        super(ClassicalGuitarTunerContent, self).__init__()
        self.notes = ["E4", "B3", "G3", "D3", "A2", "E2"]
        self.guitar_image.setGeometry(QRect(190, 10, 220, 629))
        self.guitar_image.setStyleSheet("QLabel#GuitarImageLabel { border-image: url("
                                        "./UI/Images/TunerGuitars/ClassicGuitar.png) 0 0 0 stretch stretch; }")
        self.init_notes()

    def init_notes(self):
        string1 = GuitarTunerButton(self.notes[0], "1", 400, 55)
        self.notes_buttons.append(string1)
        string2 = GuitarTunerButton(self.notes[1], "2", 400, 110)
        self.notes_buttons.append(string2)
        string3 = GuitarTunerButton(self.notes[2], "3", 400, 165)
        self.notes_buttons.append(string3)
        string4 = GuitarTunerButton(self.notes[3], "4", 150, 165)
        self.notes_buttons.append(string4)
        string5 = GuitarTunerButton(self.notes[4], "5", 150, 110)
        self.notes_buttons.append(string5)
        string6 = GuitarTunerButton(self.notes[5], "6", 150, 55)
        self.notes_buttons.append(string6)
        for button in self.notes_buttons:
            button.setParent(self)
