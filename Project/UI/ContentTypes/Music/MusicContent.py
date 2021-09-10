import threading
import time
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QFileDialog, QLabel
from Project import Recording
from Project.UI.CommonWidgets.WidgetsFactory import font_factory
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content
from Project.UI.ContentTypes.Music.CommonClass import MusicButton, PlayButton
from playsound import playsound


class MusicContent(Content):
    def __init__(self):
        super(MusicContent, self).__init__()
        self.notes_buttons = []
        self.used_threads = []
        self.finger_pick_buttons = []
        self.current_fp_buttons = []

        self.play = []

        self.notes = ["A", "Ab", "B", "Bb", "C", "D", "Db", "E", "Eb", "F", "G", "Gb"]
        self.finger_pick = ["Fingers", "Pick"]
        self.type = ["7", "maj", "min"]
        self.current_type = "0"
        self.current_fp = "0"
        self.current_notes = "0"
        #self.play_note()
        self.init_notes()

    def zero_all_notes(self):
        for button in self.notes_buttons:
            button.setStyleSheet(button.start_style)


    def zero_all_finger_pick(self):
        for button in self.finger_pick_buttons:
            button.setStyleSheet(button.start_style)

    def zero_all_type(self):
        for button in self.current_fp_buttons:
            button.setStyleSheet(button.start_style)

    def init_notes(self):
        string1 = MusicButton(self.notes[0], "1", 400, 55)
        self.notes_buttons.append(string1)
        string2 = MusicButton(self.notes[1], "2", 400, 110)
        self.notes_buttons.append(string2)
        string3 = MusicButton(self.notes[2], "3", 400, 165)
        self.notes_buttons.append(string3)
        string4 = MusicButton(self.notes[3], "4", 150, 165)
        self.notes_buttons.append(string4)
        string5 = MusicButton(self.notes[4], "5", 150, 110)
        self.notes_buttons.append(string5)
        string6 = MusicButton(self.notes[5], "6", 150, 55)
        self.notes_buttons.append(string6)
        string7 = MusicButton(self.notes[6], "6", 400, 210)
        self.notes_buttons.append(string7)

        string8 = MusicButton(self.notes[7], "7", 400, 265)
        self.notes_buttons.append(string8)
        string9 = MusicButton(self.notes[8], "8", 400, 310)
        self.notes_buttons.append(string9)
        string10 = MusicButton(self.notes[9], "9", 150, 210)
        self.notes_buttons.append(string10)
        string11 = MusicButton(self.notes[10], "10", 150, 265)
        self.notes_buttons.append(string11)
        string12 = MusicButton(self.notes[11], "11", 150, 310)
        self.notes_buttons.append(string12)

        finger_bot = MusicButton(self.finger_pick[0], "1", 400, 400)
        self.finger_pick_buttons.append(finger_bot)
        pick_bot = MusicButton(self.finger_pick[1], "2", 150, 400)
        self.finger_pick_buttons.append(pick_bot)

        regular = MusicButton(self.type[0], "1", 400, 450)
        self.current_fp_buttons.append(regular)
        minor = MusicButton(self.type[1], "2", 400, 500)
        self.current_fp_buttons.append(minor)
        major = MusicButton(self.type[2], "3", 150, 500)
        self.current_fp_buttons.append(major)

        play = PlayButton("PLAY", "3", 0, 0)
        self.play.append(play)
        play.setParent(self)


        for button in self.notes_buttons:
            button.setParent(self)
        for button in self.current_fp_buttons:
            button.setParent(self)
        for button in self.finger_pick_buttons:
            button.setParent(self)

