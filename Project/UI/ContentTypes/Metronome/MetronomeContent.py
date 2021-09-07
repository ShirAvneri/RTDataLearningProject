import threading

from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QSpinBox, QComboBox

from Project.Metronome import Metronome
from Project.UI.Content import Content


class MetronomeContent(Content):
    def __init__(self):
        super(MetronomeContent, self).__init__()
        self.metronome = Metronome(127)
        self.btn_style = "border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: white; " \
                         "border-radius: 25px; "
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)

        self.start_btn = QPushButton()
        self.start_btn.setObjectName("StartBtn")
        self.start_btn.clicked.connect(self.start_with_thread)
        self.start_btn.setGeometry(QRect(310, 200, 100, 100))
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("border-style: solid; border-width: 1px; border-color: #c9c9c9; "
                                     "background-color: white; border-radius: 50px; ")
        self.start_btn.setText("Start")

        self.stop_btn = QPushButton()
        self.start_btn.setObjectName("StopBtn")
        self.stop_btn.clicked.connect(self.metronome.stop)
        self.stop_btn.setGeometry(QRect(190, 200, 100, 100))
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet("border-style: solid; border-width: 1px; border-color: #c9c9c9; background-color: "
                                    "white; border-radius: 50px;")
        self.stop_btn.setText("Stop")

        self.start_btn.setParent(self)
        self.stop_btn.setParent(self)

        self.bpm_spinbox = QSpinBox(self)
        self.bpm_spinbox.displayIntegerBase()
        self.bpm_spinbox.setMinimum(70)
        self.bpm_spinbox.setMaximum(300)
        self.bpm_spinbox.setGeometry(QRect(250, 100, 100, 25))
        self.bpm_spinbox.setFont(font)

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
