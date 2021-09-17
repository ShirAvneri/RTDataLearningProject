from PySide6.QtCore import QRect
from Project.UI.ContentTypes.GuitarTuner.CommonClasses import GuitarTunerButton
from Project.UI.ContentTypes.GuitarTuner.GuitarTunerContent import GuitarTunerContent


class ClassicalGuitarTunerContent(GuitarTunerContent):
    def __init__(self):
        super(ClassicalGuitarTunerContent, self).__init__()
        self.guitar_image.setGeometry(QRect(190, 10, 220, 629))
        self.guitar_image.setStyleSheet("QLabel#GuitarImageLabel { border-image: url("
                                        "./UI/Images/TunerGuitars/ClassicGuitar.png) 0 0 0 stretch stretch; }")
        self.init_notes()

    def zero_all(self, note):
        for button in self.notes_buttons:
            if button != note:
                if button.is_clicked:
                    button.is_clicked = False
                    button.is_tuning = True
                    button.setText(button.note)
                    button.setStyleSheet("QPushButton#" + button.name + " { " + button.style + " }")

    def init_notes(self):
        string3 = GuitarTunerButton(self.notes[3], "1", 400, 55)
        string2 = GuitarTunerButton(self.notes[4], "2", 400, 110)
        string1 = GuitarTunerButton(self.notes[5], "3", 400, 165)
        string6 = GuitarTunerButton(self.notes[0], "4", 150, 165)
        string5 = GuitarTunerButton(self.notes[1], "5", 150, 110)
        string4 = GuitarTunerButton(self.notes[2], "6", 150, 55)
        self.notes_buttons.append(string1)
        self.notes_buttons.append(string2)
        self.notes_buttons.append(string3)
        self.notes_buttons.append(string4)
        self.notes_buttons.append(string5)
        self.notes_buttons.append(string6)
        for button in self.notes_buttons:
            button.setParent(self)

