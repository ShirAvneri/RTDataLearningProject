from PySide6.QtWidgets import QLabel

from Project.UI.Content import Content


class GuitarTunerContent(Content):
    def __init__(self):
        super(GuitarTunerContent, self).__init__()
        self.notes = None
        self.notes_buttons = []
        self.guitar_image = QLabel(self)
        self.guitar_image.setObjectName("GuitarImageLabel")

    def change_notes(self, notes: []):
        for i, _ in enumerate(self.notes_buttons):
            self.notes[i] = notes[i]
            self.notes_buttons[i].change_note(notes[i], str(i + 1))

    def tune_note(self, note):
        # TO-DO:
        # When this function is called, it will invoke the backend tuner function
        # Connect this function to buttons
        pass
