import os
from Project.UI.Enums import TopBarSignals

OS_PATH = os.path.join(os.path.dirname(__file__))
IMAGES_PATH = os.path.join(os.path.dirname(__file__), 'UI', 'Images')
GUITAR_TYPES = {"Classic Guitar": 0, "Acoustic Guitar": 1, "Electric Guitar": 2}
TOP_BAR_FUNCTIONALITY = {"Guitar Tuning": TopBarSignals.GUITAR_TUNING_CLICK,
                         "Recording": TopBarSignals.RECORDING_CLICK,
                         "Chord Detection": TopBarSignals.CHORD_DETECTION_CLICK,
                         "Metronome": TopBarSignals.METRONOME_CLICK,
                         "Audio Analysis": TopBarSignals.AUDIO_ANALYSIS_CLICK,
                         "Pitch Training": TopBarSignals.PITCH_TRAINING_CLICK}
ClosetNote = "E4"
CURRENT_PITCH = 0.0
NOTE_PITCH = 0.0



