from PySide6.QtWidgets import QMainWindow
from sympy.core import singleton

from Project.UI.ContentTypes.ChordDetection.ChordDetectionContent import ChordDetectionContent
from Project.UI.ContentTypes.GuitarTuner.AcousticGuitarTunerContent import AcousticGuitarTunerContent
from Project.UI.ContentTypes.GuitarTuner.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.ContentTypes.GuitarTuner.ElectricGuitarTunerContent import ElectricGuitarTunerContent
from Project.UI.ContentTypes.Metronome.MetronomeContent import MetronomeContent
from Project.UI.ContentTypes.Music.MusicContent import MusicContent
from Project.UI.ContentTypes.Recording.RecordingContent import RecordingContent
from Project.UI.ContentTypes.SongUpload.SongUploadContent import SongUploadContent
from Project.UI.Enums import TunerSignals, TopBarSignals
from Project.UI.MediatorPattern import GuiMediator
from Project.UI.SideMenuTypes.GuitarTunerSideMenu import GuitarTunerSideMenu
from Project.UI.SideMenuTypes.MetronomeSideMenu import MetronomeSideMenu
from Project.UI.TopBarComponent import TopBar


class AppMainWindow(QMainWindow):
    def __init__(self):
        super(AppMainWindow, self).__init__()
        self.setFixedSize(900, 600)
        self.setWindowTitle("CSMusic App")
        self.top_bar = None
        self.side_menu = None
        self.content = None
        self.init_gui_components()

    def init_gui_components(self):
        self.top_bar = TopBar()
        self.top_bar.setParent(self)
        self.side_menu = GuitarTunerSideMenu()
        self.side_menu.setParent(self)
        self.content = ClassicalGuitarTunerContent()
        self.content.setParent(self)
        GuiMediator(self, self.top_bar, self.side_menu, self.content)

    def change_tuner(self, signal_type: TunerSignals):
        self.content.setParent(None)
        if signal_type == TunerSignals.CHANGE_TUNER_TO_CLASSIC:
            self.content = ClassicalGuitarTunerContent()
        elif signal_type == TunerSignals.CHANGE_TUNER_TO_ELECTRIC:
            self.content = ElectricGuitarTunerContent()
        else:
            self.content = AcousticGuitarTunerContent()
        self.content.setParent(self)
        self.content.show()

    def change_app_functionality(self, signal_type: TopBarSignals):
        self.content.setParent(None)
        if self.side_menu is not None:
            self.side_menu.setParent(None)

        if signal_type == TopBarSignals.GUITAR_TUNING_CLICK:
            self.content = ClassicalGuitarTunerContent()
            self.side_menu = GuitarTunerSideMenu()
        elif signal_type == TopBarSignals.RECORDING_CLICK:
            self.content = RecordingContent(True)
            self.side_menu = None
        elif signal_type == TopBarSignals.CHORD_DETECTION_CLICK:
            self.content = ChordDetectionContent(True)
            self.side_menu = None
        elif signal_type == TopBarSignals.METRONOME_CLICK:
            self.content = MetronomeContent()
            self.side_menu = MetronomeSideMenu()
        elif signal_type == TopBarSignals.UPLOAD_CLICK:
            self.content = SongUploadContent(True)
            self.side_menu = None
        else:
            self.content = MusicContent(True)
            self.side_menu = None
        self.content.setParent(self)
        self.content.show()
        if self.side_menu is not None:
            self.side_menu.setParent(self)
            self.side_menu.show()
