import os
import threading
from pydub import AudioSegment
from pydub.playback import play
from Project.UI.CommonWidgets.CommonButtons import RadioButtonsGroup, StartStopButton
from Project.UI.CommonWidgets.CommonLabels import Label, CardLabel
from Project.UI.ContentComponent import Content


class PitchTrainingContent(Content):
    def __init__(self, is_full_screen):
        super(PitchTrainingContent, self).__init__(is_full_screen)
        self.audio_thread = None
        self.chords = ["A", "Ab", "B", "Bb", "C", "D", "Db", "E", "Eb", "F", "G", "Gb"]
        self.intervals = ["maj", "min", "7"]
        self.styles = ["Fingers", "Pick"]
        self.radio_buttons = {
            "Chords": RadioButtonsGroup(invoke_on_click=None, click_signal=None, x_pos=50, y_pos=85,
                                        buttons_names=self.chords),
            "Intervals": RadioButtonsGroup(invoke_on_click=None, click_signal=None, x_pos=350, y_pos=85,
                                           buttons_names=self.intervals),
            "Styles": RadioButtonsGroup(invoke_on_click=None, click_signal=None, x_pos=650, y_pos=85,
                                        buttons_names=self.styles)
        }
        self.play_button = StartStopButton(start_function=self.set_audio, stop_function=None, start_text="PLAY",
                                           stop_text="PLAYING")
        self.play_button.setParent(self)
        self.play_button.init_style("MusicButtonController", 400, 400)
        self.init_content()

    def init_content(self):
        CardLabel(self, 25, 40, "./UI/Images/Guitars/HalfClassicGuitar.png")
        chords_label = Label(50, 55, "CHOOSE A CHORD")
        chords_label.setParent(self)
        CardLabel(self, 325, 40, "./UI/Images/Guitars/HalfAcousticGuitar.png")
        intervals_label = Label(350, 55, "CHOOSE AN INTERVAL")
        intervals_label.setParent(self)
        CardLabel(self, 625, 40, "./UI/Images/Guitars/HalfElectricGuitar.png")
        styles_label = Label(650, 55, "CHOOSE A STYLE")
        styles_label.setParent(self)
        for key in self.radio_buttons.keys():
            self.radio_buttons[key].setParent(self)
            self.radio_buttons[key].set_buttons()

    def init_selection(self):
        for key in self.radio_buttons.keys():
            self.radio_buttons[key].init_selected_button()

    def set_audio(self):
        self.play_button.setEnabled(False)
        chord = self.radio_buttons["Chords"].checkedButton().text()
        interval = self.radio_buttons["Intervals"].checkedButton().text()
        style = self.radio_buttons["Styles"].checkedButton().text()
        file_path = str(os.path.abspath(os.curdir)).replace("\\", "/") + f"/Guitar Samples/Guitar Samples/{style}/" \
                                                                         f"{chord}/{chord} {interval}.wav"
        self.audio_thread = threading.Thread(target=self.play_audio, args=(file_path,))
        self.audio_thread.start()

    def play_audio(self, file_path):
        song = AudioSegment.from_wav(file_path)
        play(song)
        self.stop_audio()

    def stop_audio(self):
        self.play_button.setText(self.play_button.start_text)
        self.play_button.setStyleSheet(self.play_button.start_style)
        self.play_button.is_start = True
        self.play_button.setEnabled(True)


