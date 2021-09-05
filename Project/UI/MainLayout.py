from Project.UI.ContentTypes.ChordDetectionContent import ChordDetectionContent
from Project.UI.ContentTypes.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.SideMenu import *
from Project.UI.TopBar import *
from Project.UI.Content import *
from Project.Constants import *


class MainLayout(QWidget):
    def __init__(self, width, height):
        super(MainLayout, self).__init__()
        self.setGeometry(0, 0, width, height)
        self.side_menu = SideMenu()
        self.top_bar = TopBar()
        self.content = Content()

    def init_layout(self):
        self.side_menu.setParent(self)
        self.top_bar.setParent(self)
        self.content = ClassicalGuitarTunerContent()
        self.content.setParent(self)

    def change_content(self, content_type):
        new_content = None
        if content_type == GUITAR_TUNING:
            self.content.setParent(None)
            new_content = ClassicalGuitarTunerContent()
        elif content_type == CLASSICAL_GUITAR_TUNER:
            self.content.setParent(None)
            new_content = ClassicalGuitarTunerContent()
        elif content_type == ELECTRIC_GUITAR_TUNER:
            self.content.setParent(None)
            new_content = ClassicalGuitarTunerContent()
        elif content_type == ACOUSTIC_GUITAR_TUNER:
            self.content.setParent(None)
            new_content = ClassicalGuitarTunerContent()
        elif content_type == CHORD_DETECTION:
            self.content.setParent(None)
            new_content = ChordDetectionContent()
        elif content_type == RECORDING:
            self.content.setParent(None)
            new_content = ClassicalGuitarTunerContent()
        new_content.setParent(self)
        self.content = new_content
        self.content.show()

    def change_tuning(self, notes):
        self.content.change_notes(notes)
