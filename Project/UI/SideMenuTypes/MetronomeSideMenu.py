from Project.UI.CommonWidgets.CommonButtons import RadioButtonsGroup
from Project.UI.CommonWidgets.CommonLabels import Label
from Project.UI.Enums import SideMenuEvents
from Project.UI.SideMenuComponent import SideMenu


# BPM Taken from: https://www.musical-u.com/learn/rhythm-tips-for-identifying-music-genres-by-ear/


class MetronomeSideMenu(SideMenu):
    def __init__(self):
        super(MetronomeSideMenu, self).__init__()
        self.chooseGenreLabel = Label(self, 10, 60, "CHOOSE A GENRE")
        self.chooseGenreLabel.setParent(self)
        self.genres_list = {  # (min_bpm, max_bpm)
            "None": (70, 300),
            "Waltz ": (84, 90),
            "Tango ": (62, 66),
            "Cha Cha Cha ": (120, 128),
            "Rumba ": (100, 108),
            "Samba ": (96, 104),
            "Salsa ": (180, 300),
            "Paso Doble ": (120, 124),
            "Jazz ": (120, 125),
            "Reggae ": (60, 90),
            "Pop": (100, 130),
            "R&B": (60, 80),
            "Rock": (110, 140),
            "Metal": (100, 160),
            "Hip Hop": (85, 115),
            "House": (118, 135),
            "Trance": (130, 145),
            "Dubstep": (138, 142),
            "Trap": (138, 142),
            "Techno": (120, 160),
        }
        self.radio_buttons = RadioButtonsGroup(invoke_on_click=self.notify,
                                               click_signal=SideMenuEvents.CHANGE_GENRE,
                                               x_pos=20, y_pos=90,
                                               buttons_names=self.genres_list.keys())
        self.radio_buttons.setParent(self)
        self.radio_buttons.set_buttons()

    def notify(self, event_signal, genre):
        self.mediator.notify(event_signal, self.genres_list[genre])
