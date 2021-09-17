from PySide6.QtWidgets import QLabel

from Project.UI import ContentComponent


class GuitarTunerContent(ContentComponent.Content):
    def __init__(self):
        super(GuitarTunerContent, self).__init__()
        #  TO DO:
        #  verify the standard tuning for all guitar types.
        self.notes = ["E2", "A2", "D3", "G3", "B3", "E4"]
        self.notes_buttons = []
        self.guitar_image = QLabel(self)
        self.guitar_image.setObjectName("GuitarImageLabel")

    def change_notes(self, notes: []):
        for i, _ in enumerate(self.notes_buttons):
            self.notes[i] = notes[i]
            self.notes_buttons[i].change_note(notes[i], str(i + 1))

    def tune_note(self, note):
        # TO DO:
        # When this function is called, it will invoke the backend tuner function
        # Connect this function to buttons
        pass
