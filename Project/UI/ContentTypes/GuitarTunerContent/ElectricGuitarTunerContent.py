from PySide6.QtCore import QRect
from Project.UI.ContentTypes.GuitarTunerContent.CommonClasses import GuitarTunerButton
from Project.UI.ContentTypes.GuitarTunerContent.GuitarTunerContent import GuitarTunerContent


class ElectricGuitarTunerContent(GuitarTunerContent):
    def __init__(self):
        super(ElectricGuitarTunerContent, self).__init__()
        self.notes = ["1", "2", "3", "4", "5", "6"]
        self.guitar_image.setGeometry(QRect(150, 30, 300, 630))
        self.guitar_image.setStyleSheet("QLabel#GuitarImageLabel { border-image: url("
                                        "./UI/Images/TunerGuitars/ElectricGuitar.png) 0 0 0 stretch stretch; }")
        self.init_notes()

    def init_notes(self):
        string1 = GuitarTunerButton(self.notes[0], "1", 285, 5)
        self.notes_buttons.append(string1)
        string2 = GuitarTunerButton(self.notes[1], "2", 250, 45)
        self.notes_buttons.append(string2)
        string3 = GuitarTunerButton(self.notes[2], "3", 215, 85)
        self.notes_buttons.append(string3)
        string4 = GuitarTunerButton(self.notes[3], "4", 180, 125)
        self.notes_buttons.append(string4)
        string5 = GuitarTunerButton(self.notes[4], "5", 145, 165)
        self.notes_buttons.append(string5)
        string6 = GuitarTunerButton(self.notes[5], "6", 110, 205)
        self.notes_buttons.append(string6)
        for button in self.notes_buttons:
            button.setParent(self)
