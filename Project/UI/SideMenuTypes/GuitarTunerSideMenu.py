import json

from Project.Constants import GUITAR_TYPES
from Project.UI.SideMenu import SideMenu
from Project.UI.SideMenuTypes.CommonClasses import *


class GuitarTunerSideMenu(SideMenu):
    def __init__(self):
        super(GuitarTunerSideMenu, self).__init__()
        self.tunings_list = ["Standard", "Drop D", "Drop C", "Drop C#", "Drop B", "Drop A", "DADGAD", "Half Step Down",
                             "Full Step Down", "Half Step Up", "Open C", "Open D", "Open E", "Open F", "Open G",
                             "Open A"]
        self.chooseInstrumentLabel = SideMenuLabel(10, 60, "CHOOSE AN INSTRUMENT")
        self.chooseInstrumentLabel.setParent(self)
        self.classicalBtn = SideMenuGuitarButton(GUITAR_TYPES["Classic Guitar"], 20, 85)
        self.classicalBtn.set_icon("./UI/Images/GuitarIcons/ClassicGuitarIcon.png")
        self.classicalBtn.setParent(self)
        self.acousticBtn = SideMenuGuitarButton(GUITAR_TYPES["Acoustic Guitar"], 110, 85)
        self.acousticBtn.set_icon("./UI/Images/GuitarIcons/AcousticGuitarIcon.png")
        self.acousticBtn.setParent(self)
        self.electricBtn = SideMenuGuitarButton(GUITAR_TYPES["Electric Guitar"], 200, 85)
        self.electricBtn.set_icon("./UI/Images/GuitarIcons/ElectricGuitarIcon.png")
        self.electricBtn.setParent(self)
        self.chooseTuningLabel = SideMenuLabel(10, 180, "CHOOSE TUNING")
        self.chooseTuningLabel.setParent(self)
        self.radio_buttons = SideMenuRadioButtons(20, 205, self.change_tuning, self.tunings_list)
        self.radio_buttons.setParent(self)
        self.radio_buttons.set_buttons()

    def guitar_change_event(self, guitar_type):
        self.radio_buttons.init_selected_button()
        self.parent().guitar_change_event_handler(guitar_type)

    def change_tuning(self, tuning):
        f = open('./UI/TuningNotes.json', )
        tunings = json.load(f)
        self.parent().tuning_change_event_handler(tunings[tuning])
