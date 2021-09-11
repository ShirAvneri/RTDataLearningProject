import threading

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QSpinBox, QComboBox

from Project.Metronome import Metronome
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.ContentComponent import Content


class MetronomeContent(Content):
    def __init__(self):
        super(MetronomeContent, self).__init__()
        self.metronome = Metronome(127)
        self.is_running = False

        self.metronome_button = StartStopButton(self.start_with_thread, self.metronome.stop)
        self.metronome_button.setParent(self)
        self.metronome_button.init_style("MetronomeController", 250, 200)

        self.bpm_spinbox = QSpinBox(self)
        self.bpm_spinbox.displayIntegerBase()
        self.bpm_spinbox.setGeometry(QRect(250, 100, 100, 25))
        self.set_min_max(70, 300)

        self.bpb_combobox = QComboBox()
        self.bpb_combobox.setPlaceholderText("Select BPB")
        self.bpb_combobox.setGeometry(QRect(250, 150, 100, 25))
        self.bpb_combobox.setParent(self)
        self.bpb_combobox.addItems(["2/4", "3/4", "4/4", "5/4", "6/4", "7/4", "8/4"])

    def start_with_thread(self):
        self.metronome.bpm = int(self.bpm_spinbox.text())
        bpb_index = self.bpb_combobox.currentIndex()
        if bpb_index == -1:  # bpb not selected
            bpb_index = 2
        self.metronome.bpb = self.metronome.supported_bpb[bpb_index]
        threading.Thread(target=self.metronome.start).start()

    def set_min_max(self, min_bpm, max_bpm):
        self.bpm_spinbox.cleanText()
        self.bpm_spinbox.setRange(min_bpm, max_bpm)
