from PySide6.QtCore import QThread, Signal

from Project import Constants
from Project.Tuner import better_tuner


class TuningThread(QThread):

    any_signal = Signal(str)

    def __init__(self, ChordDetectionContent, parent=None, index=0):
        super(TuningThread, self).__init__(parent)
        self.ChordDetectionContent = ChordDetectionContent

    def run(self):
        while True:
            # print(self.flag)
            if self.flag:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
                break
            # self.setEnabled(False)
            better_tuner()
            # self.setEnabled(True)
            # print("***********************")
            print(Constants.ClosetNote)
            if Constants.ClosetNote[0] < self.note[0]:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_red + " }")
                print("in red")
                self.setText("UP")
                if self.flag:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style + " }")
                    break
            elif Constants.ClosetNote[0] == self.note[0]:
                # self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_OK + " }")
                number_in_cur_note = Constants.ClosetNote[1]
                number_in_note = self.note[1]
                if number_in_note == "#":
                    number_in_note = self.note[2]
                if number_in_cur_note == "#":
                    number_in_note = Constants.ClosetNote[2]
                if number_in_cur_note < number_in_note:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_yellow + " }")
                    self.setText("UP")
                elif number_in_cur_note == number_in_note:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_green + " }")
                    self.setText(self.note)
                else:
                    self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_yellow + " }")
                    self.setText("DOWN")

                print("in Ylow")

            else:
                self.setStyleSheet("QPushButton#" + self.name + " { " + self.style_red + " }")
                print("in green")
                self.setText("DOWN")
        print("end tuner")
        self.setText(self.note)