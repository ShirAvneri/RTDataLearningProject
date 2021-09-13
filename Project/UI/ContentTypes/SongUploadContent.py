from PySide6.QtCore import QRect
from PySide6.QtWidgets import QVBoxLayout, QPlainTextEdit
from Project.ChordDetector.ChordDetection.chroma_chord_detection import chord_detection_prefilepath
from Project.UI.CommonWidgets.CommonButtons import FilePickerButton
from Project.UI.ContentComponent import Content
from Project.UI.ContentTypes.ChordDetection.CommonClasses import ChordAnalyzingButton


class SongUploadContent(Content):
    def __init__(self, is_full_screen):
        super(SongUploadContent, self).__init__(is_full_screen)
        self.vBOX = QVBoxLayout()
        self.counter = 1
        text = "Detected Chord:"
        self.chord_text = QPlainTextEdit()
        self.vBOX.setGeometry(QRect(50, 50, 50, 50))

        self.chord_text.appendPlainText(text)
        # self.chord_text.setPlainText("**********************")
        self.chord_text.setReadOnly(True)
        self.vBOX.addWidget(self.chord_text)
        self.setLayout(self.vBOX)

        self.buttons = []
        self.path = "a"
        self.upload_button = FilePickerButton()
        self.buttons.append(self.upload_button)
        self.upload_button.setParent(self)
        self.upload_button.init_style("MetronomeController", 250, 400)
        self.analyze_button = ChordAnalyzingButton(200, 400)
        self.analyze_button.setParent(self)
        self.analyze_button.clicked.connect(self.analyze)
        self.thread = None
        self.process = None
        self.stream = None
        self.p = None
        self.flag = False
        self.analyze_button.path = self.path
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(130, 50, 260, 500))
        # text.setText('note detected: ')
        # text = QLabel(self)
        # text.setObjectName("GuitarImageLabel")
        # text.setGeometry(QRect(220, 50, 260, 500))
        # text.setText('NOTE')

    def analyze(self):
        print(self.upload_button.path[0])

        if self.upload_button.path == "":
            return
        else:
            self.chord_text.appendPlainText("Iteration number:" + str(self.counter))
            print("*******************")
            return_list = chord_detection_prefilepath(self.upload_button.path[0])
            # self.chord_text.appendPlainText(str(*chord_detection_prefilepath(self.upload_button.path[0]), sep=", "))
            for x in range(len(return_list)):
                self.chord_text.appendPlainText(str(return_list[x]))
            self.counter += 1