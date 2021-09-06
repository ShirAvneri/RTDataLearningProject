from PySide6.QtWidgets import QWidget

from Project.UI.Content import Content
from Project.UI.ContentTypes.ChordDetection.ChordDetectionContent import ChordDetectionContent
from Project.UI.ContentTypes.GuitarTuner.AcousticGuitarTunerContent import AcousticGuitarTunerContent
from Project.UI.ContentTypes.GuitarTuner.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.ContentTypes.GuitarTuner.ElectricGuitarTunerContent import ElectricGuitarTunerContent
from Project.UI.ContentTypes.Recording.RecordingContent import RecordingContent
from Project.UI.SideMenu import SideMenu
from Project.UI.TopBar import TopBar
from Project.Constants import GUITAR_TYPES, TOP_BAR_FUNCTIONALITY


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

    def change_content(self, new_content):
        self.content.setParent(None)
        new_content.setParent(self)
        self.content = new_content
        self.content.show()

    def tuning_change_event_handler(self, notes):
        self.content.change_notes(notes)

    def guitar_change_event_handler(self, guitar_type):
        if guitar_type == GUITAR_TYPES["Classic Guitar"]:
            new_content = ClassicalGuitarTunerContent()
        elif guitar_type == GUITAR_TYPES["Electric Guitar"]:
            new_content = ElectricGuitarTunerContent()
        else:
            new_content = AcousticGuitarTunerContent()
        self.change_content(new_content)

    def top_bar_event_handler(self, functionality):
        if functionality == TOP_BAR_FUNCTIONALITY["Guitar Tuning"]:
            new_content = ClassicalGuitarTunerContent()
        elif functionality == TOP_BAR_FUNCTIONALITY["Recording"]:
            new_content = RecordingContent()
        else:
            new_content = ChordDetectionContent()
        self.change_content(new_content)
