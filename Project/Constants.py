from Project.UI.Enums import TopBarSignals

GUITAR_TYPES = {"Classic Guitar": 0, "Acoustic Guitar": 1, "Electric Guitar": 2}
TOP_BAR_FUNCTIONALITY = {"Guitar Tuning": TopBarSignals.GUITAR_TUNING_CLICK,
                         "Recording": TopBarSignals.RECORDING_CLICK,
                         "Chord Detection": TopBarSignals.CHORD_DETECTION_CLICK,
                         "Metronome": TopBarSignals.METRONOME_CLICK,
                         "Upload": TopBarSignals.UPLOAD_CLICK,
                         "Music": TopBarSignals.MUSIC_CLICK}
ClosetNote = "0"
