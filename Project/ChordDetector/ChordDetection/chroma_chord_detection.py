import json
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from Project.ChordDetector.ChordDetection.chromagram import extract_pitch_chroma, block_audio, compute_stft, file_read, file_normalize

# Loading the JSON into a variable
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

with open('chord_template.json', 'r') as fp:
    templates_json = json.load(fp)

cutoff = 0.1
NUMBER_OF_CHORDS = 32
# List of 36 common chord classes
chords = ['N', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#',
            'D','D#', 'E', 'E7', 'F', 'F#', 'Gm', 'G#m', 'Am',
            'A#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm'
            , "Cadd9", "Fsus2", "Dsus4", "Em7",
          "Am7", 'F#m', 'A7', "Dsus2"]

# chords = ['N', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#',
#             'D','D#', 'E', 'F', 'F#', 'Gm', 'G#m', 'Am',
#             'A#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m']

templates = []

# Setting the block size, hop size for windowing signal and reference frequency for calculating PCP
block_size = 8192
hop_size = 1024

reference_frequency = 440


def chord_detection_filepath(filepath):

    for chord in chords:
        if chord == 'N':
            continue
        templates.append(templates_json[chord])

    fs, x = file_read(filepath)
    if len(x.shape) > 1:
        x = x[:, 1]

    xb, t = block_audio(x, block_size, hop_size, fs)
    X, fs = compute_stft(xb, fs, block_size, hop_size)

    chroma = extract_pitch_chroma(X, fs, reference_frequency)

    # print(chroma)
    chroma_template = np.mean(chroma, axis=1)

    for i in range(len(chroma_template)):
        if chroma_template[i] < cutoff:
            chroma_template[i] = 0
    #print(chroma_template)
    """Correlate 12D chroma vector with each of 24 major and minor chords"""
    cor_vec = np.zeros(NUMBER_OF_CHORDS)
    for idx in range(NUMBER_OF_CHORDS):
        cor_vec[idx] = np.dot(chroma_template, np.array(templates[idx]))
    idx_max_cor = np.argmax(cor_vec)
    #print(cor_vec)

    idx_chord = int(idx_max_cor + 1)
    chord_name = (chords[idx_chord])
    # print(chord_name)
    # # Plotting all figures
    # plt.figure(1)
    # notes = ['G','G#','A','A#','B','C','C#','D','D#','E','F','F#']
    # plt.xticks(np.arange(12),notes)
    # plt.title('Pitch Class Profile')
    # plt.xlabel('Notes')
    # plt.ylim((0.0,1.0))
    # plt.grid(True)
    # plt.plot(notes, chroma_template)
    # plt.show()
    return chord_name


def chord_detection_prefilepath(filepath, test_sound_len = 10):
    list = []
    for chord in chords:
        if chord == 'N':
            continue
        templates.append(templates_json[chord])

    fs, x = file_read(filepath)
    if len(x.shape) > 1:
        x = x[:, 1]
    xb, t = block_audio(x, block_size, hop_size, fs)
    iterations = 0
    current_chords = []
    for i in range(0, len(xb) - test_sound_len, test_sound_len):

        X, fs = compute_stft(xb[i:i+test_sound_len], fs, block_size, hop_size)

        chroma = extract_pitch_chroma(X, fs, reference_frequency)
        #print(chroma)
        chroma_template = np.mean(chroma, axis=1)
        #print(chroma_template)
        for i in range(len(chroma_template)):
            if chroma_template[i] < cutoff:
                chroma_template[i] = 0
        """Correlate 12D chroma vector with each of 24 major and minor chords"""
        cor_vec = np.zeros(NUMBER_OF_CHORDS)
        for idx in range(NUMBER_OF_CHORDS):
            cor_vec[idx] = np.dot(chroma_template, np.array(templates[idx]))
        #print(cor_vec)
        idx_max_cor = np.argmax(cor_vec)
        idx_chord = int(idx_max_cor + 1)
        chord_name = (chords[idx_chord])

        current_chords.append(str(chord_name))
        iterations += 1
        if iterations == 9:
            iterations = 0
            #print("Estimated chord: " + max(chords, key=chords.count))
            # print(chords)
            list.append(max(chords, key=current_chords.count))
            current_chords.clear()

        # # Plotting all figures
        # plt.figure(1)
        # notes = ['G','G#','A','A#','B','C','C#','D','D#','E','F','F#']
        # plt.xticks(np.arange(12),notes)
        # plt.title('Pitch Class Profile')
        # plt.xlabel('Notes')
        # plt.ylim((0.0,1.0))
        # plt.grid(True)
        # plt.plot(notes, chroma_template)
        # plt.show()

    return list


if __name__ == "__main__":
    count = 0

    folderpath = "/Users/marketinggramusic/Documents/Sem1/MIR/Project/crs/single-chord-dataset/"

    for folder in listdir(folderpath):
        if folder != ".DS_Store":
            filepath = os.path.join(folderpath, folder)
            if filepath != ".DS_Store":
                for file in listdir(filepath):
                    if file != ".DS_Store":
                        file_path = os.path.join(filepath,file)
                        chord = chord_detection_filepath(file_path)
                        print("Estimated: " + str(chord) + "    |    " + "Ground Truth: " + folder)
                        # est = str(chord[0]) + " " + str(chord[1])