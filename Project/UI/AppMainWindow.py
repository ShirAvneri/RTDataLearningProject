
from PySide6.QtWidgets import QMainWindow

from Project.UI.CommonWidgets.ComponentsFactory import Factory
from Project.UI.Enums import *

from Project.UI.MediatorPattern import GuiMediator


class AppMainWindow(QMainWindow):
    def __init__(self):
        super(AppMainWindow, self).__init__()
        self.setFixedSize(900, 600)
        self.setWindowTitle("CSMusic App")
        self.top_bar = None
        self.side_menu = None
        self.content = None
        self.init_gui_components()


    #@pyqtSlot(str)
    def my_function(self, chord):
        print('in my_function with signal:' + chord)
        self.content.append_text(chord)

    def init_gui_components(self):
        self.top_bar = Factory.create_top_bar()
        self.top_bar.setParent(self)
        self.side_menu = Factory.create_side_menu(AppWidgetTypes.TUNER_SIDE_MENU)
        self.side_menu.setParent(self)
        self.content = Factory.create_content(AppWidgetTypes.CLASSIC_TUNER_CONTENT)
        self.content.setParent(self)
        GuiMediator(self, self.top_bar, self.side_menu, self.content)

    def change_tuner(self, signal_type: TunerSignals):
        self.content.setParent(None)
        if signal_type == TunerSignals.CHANGE_TUNER_TO_CLASSIC:
            self.content = Factory.create_content(AppWidgetTypes.CLASSIC_TUNER_CONTENT)
        elif signal_type == TunerSignals.CHANGE_TUNER_TO_ELECTRIC:
            self.content = Factory.create_content(AppWidgetTypes.ELECTRIC_TUNER_CONTENT)
        else:
            self.content = Factory.create_content(AppWidgetTypes.ACOUSTIC_TUNER_CONTENT)
        self.content.setParent(self)
        self.content.show()

    def change_app_functionality(self, signal_type: TopBarSignals):
        self.content.setParent(None)
        if self.side_menu is not None:
            self.side_menu.setParent(None)

        if signal_type == TopBarSignals.GUITAR_TUNING_CLICK:
            self.content = Factory.create_content(AppWidgetTypes.CLASSIC_TUNER_CONTENT)
            self.side_menu = Factory.create_side_menu(AppWidgetTypes.TUNER_SIDE_MENU)
        elif signal_type == TopBarSignals.RECORDING_CLICK:
            self.content = Factory.create_content(AppWidgetTypes.RECORDING_CONTENT)
            self.side_menu = None
        elif signal_type == TopBarSignals.CHORD_DETECTION_CLICK:
            self.content = Factory.create_content(AppWidgetTypes.CHORD_DETECTION_CONTENT)
            self.side_menu = None
        elif signal_type == TopBarSignals.METRONOME_CLICK:
            self.content = Factory.create_content(AppWidgetTypes.METRONOME_CONTENT)
            self.side_menu = Factory.create_side_menu(AppWidgetTypes.METRONOME_SIDE_MENU)
        elif signal_type == TopBarSignals.UPLOAD_CLICK:
            self.content = Factory.create_content(AppWidgetTypes.UPLOAD_CONTENT)
            self.side_menu = None
        else:
            self.content = Factory.create_content(AppWidgetTypes.MUSIC_CONTENT)
            self.side_menu = None
        self.content.setParent(self)
        self.content.show()
        if self.side_menu is not None:
            self.side_menu.setParent(self)
            self.side_menu.show()

