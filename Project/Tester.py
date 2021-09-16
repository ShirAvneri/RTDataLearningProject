import os
import random
import wave

from Project.ChordDetector.ChordDetection.chroma_chord_detection import chord_detection_prefilepath


class Tester():
    def __init__(self):
        self.notes = ["A", "G#", "B", "A#", "C", "D", "C#", "E", "D#", "F", "G", "F#"]
        self.finger_pick = ["Fingers", "Pick"]
        self.type = ["7", "maj", "min"]

    def create_test_sample(self, length):
        if length > 100:
            length = 100
        data = []
        expected_output = []
        for i in range(length):
            note = self.notes[random.randrange(0, len(self.notes))]
            type = self.type[random.randrange(0, len(self.type))]
            style = "Pick"
            if type == "min":
                expected_output.append(note + "m")
            elif type == "7":
                expected_output.append(note + "7")
            else:
                expected_output.append(note)
            file_path = str(os.path.abspath(os.curdir)).replace("\\", "/") + \
                        f"/Guitar Samples/Guitar Samples/{style}/{note}/{note} {type}.wav"
            w = wave.open(file_path, 'rb')
            data.append([w.getparams(), w.readframes(w.getnframes())])
            w.close()
        output = wave.open("test.wav", 'wb')
        output.setparams(data[0][0])
        for i in range(len(data)):
            output.writeframes(data[i][1])
        output.close()
        return expected_output

    def execute_test(self, expected_output):
        chord_list = chord_detection_prefilepath("test.wav", 160)
        pure_chord_list = []
        for i in range(len(chord_list) - 1):
            pure_chord_list.append(chord_list[i])
            if chord_list[i] == chord_list[i+1]:
                i += 1

        min_length = min(len(chord_list), len(expected_output))
        for i in range(min_length):
            print("expected: " + expected_output[i] + " found: " + chord_list[i], end="")
            if expected_output[i] == chord_list[i]:
                print("  SUCCESS!")
            else:
                print("  FAILURE!")
