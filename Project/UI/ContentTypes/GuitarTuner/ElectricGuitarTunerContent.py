from PySide6.QtCore import QRect

from Project.Tuner import main_tuner
from Project.UI.ContentTypes.GuitarTuner.CommonClasses import GuitarTunerButton
from Project.UI.ContentTypes.GuitarTuner.GuitarTunerContent import GuitarTunerContent


class ElectricGuitarTunerContent(GuitarTunerContent):
    def __init__(self):
        super(ElectricGuitarTunerContent, self).__init__()
        self.guitar_image.setGeometry(QRect(150, 30, 300, 630))
        self.guitar_image.setStyleSheet("QLabel#GuitarImageLabel { border-image: url("
                                        "./UI/Images/TunerGuitars/ElectricGuitar.png) 0 0 0 stretch stretch; }")
        self.init_notes()

    def init_notes(self):
        string1 = GuitarTunerButton(self.notes[5], "1", 285, 5)
        string2 = GuitarTunerButton(self.notes[4], "2", 250, 45)
        string3 = GuitarTunerButton(self.notes[3], "3", 215, 85)
        string4 = GuitarTunerButton(self.notes[2], "4", 180, 125)
        string5 = GuitarTunerButton(self.notes[1], "5", 145, 165)
        string6 = GuitarTunerButton(self.notes[0], "6", 110, 205)

        self.notes_buttons.append(string6)
        self.notes_buttons.append(string5)
        self.notes_buttons.append(string4)
        self.notes_buttons.append(string3)
        self.notes_buttons.append(string2)
        self.notes_buttons.append(string1)

        for button in self.notes_buttons:
            button.setParent(self)
            #button.clicked.connect(self.play_tuner)

    def zero_all(self, note):
        for button in self.notes_buttons:
            if button != note:
                if button.Flag == 1:
                    button.Flag = 0
                    button.flag = True
                    button.setText(button.note)
                    button.setStyleSheet("QPushButton#" + button.name + " { " + button.style + " }")


    def play_tuner(self):
        print("in play tuner")
        main_tuner()

