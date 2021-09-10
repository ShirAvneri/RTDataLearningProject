import os
import threading
import asyncio
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import multiprocessing

from Project.UI.CommonWidgets.WidgetsFactory import font_factory


class MusicButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(MusicButton, self).__init__()
        self.Flag = 0
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.start_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                           "background-color: #00a215; border-radius: 50px;"
        self.stop_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                          "background-color: #972c2c; border-radius: 50px;"
        self.is_on=0
        self.clicked.connect(self.start_music)
        self.set_button()


    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        #self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font_factory(size=14))
        self.setStyleSheet(self.start_style)
        self.is_on=0


    def start_music(self):
        print("start tuner")
        #self.style = "background-color: red; "
        if self.is_on==1:
            self.is_on = 0
            self.setStyleSheet(self.start_style)
            if self.sender().text() in self.parent().notes:
                self.parent().current_notes = "0"
            elif self.sender().text() in self.parent().finger_pick:
                self.parent().current_fp = "0"
            elif self.sender().text() in self.parent().type:
                self.parent().current_type = "0"
        else:
            self.is_on = 1
            #self.parent().
            if self.sender().text() in self.parent().notes:
                self.parent().zero_all_notes()
                self.setStyleSheet(self.stop_style)
                self.parent().play[0].current_notes = self.sender().text()

            elif self.sender().text() in self.parent().finger_pick:
                self.parent().zero_all_finger_pick()
                self.setStyleSheet(self.stop_style)
                self.parent().play[0].current_fp = self.sender().text()

            elif self.sender().text() in self.parent().type:
                self.parent().zero_all_type()
                self.setStyleSheet(self.stop_style)
                self.parent().play[0].current_type = self.sender().text()
        print(self.sender().text())


class LOCK(object):
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def free(self):
        with self._lock:
            self.value = 0

    def lock(self):
        with self._lock:
            self.value = 1


lock = threading.Lock()

class PlayButton(QPushButton):
    def __init__(self, note, string_num, x_pos, y_pos):
        super(PlayButton, self).__init__()
        self.Flag = 0
        self.note = note
        self.name = "string" + string_num
        self.setObjectName(self.name)
        self.x = x_pos
        self.y = y_pos
        self.used_threads = []

        self.notes = ["A", "Ab", "B", "Bb", "C", "D", "Db", "E", "Eb", "F", "G", "Gb"]
        self.finger_pick = ["Fingers", "Pick"]
        self.type = ["7", "maj", "min"]
        self.current_type = "0"
        self.current_fp = "0"
        self.current_notes="0"
        self.start_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                           "background-color: #00a215; border-radius: 50px;"
        self.stop_style = "color: white; border-style: solid; border-width: 10px; border-color: #FFFFFF; " \
                          "background-color: #972c2c; border-radius: 50px;"
        #self.lock = LOCK()
        self.clicked.connect(self.play_note)
        self.set_button()


    def set_button(self):
        self.setGeometry(QRect(self.x, self.y, 50, 50))
        #self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
        self.setText(self.note)
        self.setFont(font_factory(size=14))
        self.setStyleSheet(self.start_style)
        self.is_on=0

    def play_note(self):
        self.setStyleSheet(self.stop_style)
        self.setEnabled(False)
        self.listen_to_user()

    def listen_to_user(self):
       # global lock
        if self.current_type!="0" and self.current_fp!="0" and self.current_notes!="0":
            WAV_PATH="/Guitar Samples/Guitar Samples/"+self.current_fp+"/"+self.current_notes+"/"+self.current_notes+" "+self.current_type+".wav"
            WAV_PATH = str(os.path.abspath(os.curdir)).replace("\\", "/")+WAV_PATH
            listen_thread = threading.Thread(target=self.play_play,args=(WAV_PATH,))
            self.used_threads.append(listen_thread)
            listen_thread.start()

    def play_play(self,WAV_PATH):
        song = AudioSegment.from_wav(WAV_PATH)
        play(song)
        self.setStyleSheet(self.start_style)
        self.setEnabled(True)
