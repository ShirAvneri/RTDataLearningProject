import json

from Project.UI.SideMenuComponent import SideMenu
from Project.UI.SideMenuTypes.CommonClasses import SideMenuLabel, SideMenuGuitarButton, SideMenuRadioButtons
from Project.UI.Enums import TunerSignals, SideMenuEvents


class GuitarTunerSideMenu(SideMenu):
    def __init__(self):
        super(GuitarTunerSideMenu, self).__init__()
        self.tunings_list = ["Standard", "Drop D", "Drop C", "Drop C#", "Drop B", "Drop A", "DADGAD", "Half Step Down",
                             "Full Step Down", "Half Step Up", "Open C", "Open D", "Open E", "Open F", "Open G",
                             "Open A"]
        self.chooseInstrumentLabel = SideMenuLabel(10, 60, "CHOOSE AN INSTRUMENT")
        self.chooseInstrumentLabel.setParent(self)
        self.classicalBtn = SideMenuGuitarButton(click_signal=TunerSignals.CHANGE_TUNER_TO_CLASSIC, x_pos=20, y_pos=85)
        self.classicalBtn.set_icon("./UI/Images/GuitarIcons/ClassicGuitarIcon.png")
        self.classicalBtn.setParent(self)
        self.acousticBtn = SideMenuGuitarButton(click_signal=TunerSignals.CHANGE_TUNER_TO_ACOUSTIC, x_pos=110, y_pos=85)
        self.acousticBtn.set_icon("./UI/Images/GuitarIcons/AcousticGuitarIcon.png")
        self.acousticBtn.setParent(self)
        self.electricBtn = SideMenuGuitarButton(click_signal=TunerSignals.CHANGE_TUNER_TO_ELECTRIC, x_pos=200, y_pos=85)
        self.electricBtn.set_icon("./UI/Images/GuitarIcons/ElectricGuitarIcon.png")
        self.electricBtn.setParent(self)
        self.chooseTuningLabel = SideMenuLabel(10, 180, "CHOOSE TUNING")
        self.chooseTuningLabel.setParent(self)
        self.radio_buttons = SideMenuRadioButtons(invoke_on_click=self.notify,
                                                  click_signal=SideMenuEvents.CHANGE_TUNING,
                                                  x_pos=20, y_pos=205, buttons_names=self.tunings_list)
        self.radio_buttons.setParent(self)
        self.radio_buttons.set_buttons()

    def notify(self, event_signal, tuning=None):
        if isinstance(event_signal, SideMenuEvents):
            f = open('./UI/TuningNotes.json', )
            tunings = json.load(f)
            self.mediator.notify(SideMenuEvents.CHANGE_TUNING, tunings[tuning])
        else:
            self.mediator.notify(event_signal)
