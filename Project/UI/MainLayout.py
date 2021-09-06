from Project.UI.ContentTypes.ChordDetectionContent.ChordDetectionContent import ChordDetectionContent
from Project.UI.ContentTypes.GuitarTunerContent.AcousticGuitarTunerContent import AcousticGuitarTunerContent
from Project.UI.ContentTypes.GuitarTunerContent.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.ContentTypes.GuitarTunerContent.ElectricGuitarTunerContent import ElectricGuitarTunerContent
from Project.UI.ContentTypes.RecordingContent.RecordingContent import RecordingContent
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
            new_content = ClassicalGuitarTunerContent()
        elif content_type == CLASSICAL_GUITAR_TUNER:
            new_content = ClassicalGuitarTunerContent()
        elif content_type == ELECTRIC_GUITAR_TUNER:
            new_content = ElectricGuitarTunerContent()
        elif content_type == ACOUSTIC_GUITAR_TUNER:
            new_content = AcousticGuitarTunerContent()
        elif content_type == CHORD_DETECTION:
            new_content = ChordDetectionContent()
        elif content_type == RECORDING:
            new_content = RecordingContent()
        self.content.setParent(None)
        new_content.setParent(self)
        self.content = new_content
        self.content.show()

    def tuning_change_event_handler(self, notes):
        self.content.change_notes(notes)

    def guitar_change_event_handler(self, guitar_type):
        self.change_content(guitar_type)
