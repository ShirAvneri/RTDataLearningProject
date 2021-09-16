import json
from Project.UI.CommonWidgets.CommonButtons import RadioButtonsGroup, GuitarButton
from Project.UI.CommonWidgets.CommonLabels import Label
from Project.UI.SideMenuComponent import SideMenu
from Project.UI.Enums import TunerSignals, SideMenuEvents


class GuitarTunerSideMenu(SideMenu):
    def __init__(self):
        super(GuitarTunerSideMenu, self).__init__()
        self.tunings_list = ["Standard", "Drop D", "Drop C", "Drop C#", "Drop B", "Drop A", "DADGAD", "Half Step Down",
                             "Full Step Down", "Half Step Up", "Open C", "Open D", "Open E", "Open F", "Open G",
                             "Open A"]
        self.chooseInstrumentLabel = Label(parent=self, x_pos=10, y_pos=60, text="CHOOSE AN INSTRUMENT")
        self.classicalBtn = GuitarButton(parent=self, click_signal=TunerSignals.CHANGE_TUNER_TO_CLASSIC,
                                         x_pos=20, y_pos=85, icon_path="./UI/Images/GuitarIcons/ClassicGuitarIcon.png")
        self.acousticBtn = GuitarButton(parent=self, click_signal=TunerSignals.CHANGE_TUNER_TO_ACOUSTIC,
                                        x_pos=110, y_pos=85, icon_path="./UI/Images/GuitarIcons/AcousticGuitarIcon.png")
        self.electricBtn = GuitarButton(parent=self, click_signal=TunerSignals.CHANGE_TUNER_TO_ELECTRIC,
                                        x_pos=200, y_pos=85, icon_path="./UI/Images/GuitarIcons/ElectricGuitarIcon.png")
        self.chooseTuningLabel = Label(parent=self, x_pos=10, y_pos=180, text="CHOOSE TUNING")
        self.radio_buttons = RadioButtonsGroup(invoke_on_click=self.notify,
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
            self.radio_buttons.init_selected_button()
