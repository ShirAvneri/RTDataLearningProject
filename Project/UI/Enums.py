from enum import Enum


class TunerSignals(Enum):
    CHANGE_TUNER_TO_CLASSIC = 0
    CHANGE_TUNER_TO_ELECTRIC = 1
    CHANGE_TUNER_TO_ACOUSTIC = 2


class SideMenuEvents(Enum):
    CHANGE_TUNING = 0
    CHANGE_GENRE = 1


class TopBarSignals(Enum):
    GUITAR_TUNING_CLICK = 0
    RECORDING_CLICK = 1
    CHORD_DETECTION_CLICK = 2
    METRONOME_CLICK = 3
    UPLOAD_CLICK = 4
    MUSIC_CLICK = 5
