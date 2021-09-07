import threading

from PySide6.QtWidgets import QFileDialog

from Project import Recording
from Project.UI.CommonWidgets.StartStopButton import StartStopButton
from Project.UI.Content import Content


class RecordingContent(Content):
    def __init__(self):
        super(RecordingContent, self).__init__()
        self.is_recording = False
        self.button = StartStopButton(self.start_recording, self.stop_recording)
        self.button.init_style("Recording Button", 500, 50)
        self.button.setParent(self)

    def start_recording(self):
        self.is_recording = True
        thread = threading.Thread(target=self.get_tape)
        thread.start()
        print("after start")
        #thread.join()
        print("after join")
        #thread1 = threading.Thread(target=self.save_file)
        #thread1.start()

    def stop_recording(self):
        self.is_recording = False

    def save_file(self):
        fileName = QFileDialog.getSaveFileName(self, "Save F:xile",
                                               "/home/jana/untitled.png",
                                               "Images (*.png *.xpm *.jpg)")

    def get_tape(self):
        stream, p = Recording.open_stream()
        frames = []
        while self.is_recording:
            Recording.get_stream(stream, p, frames)
        Recording.end_stream(stream, p, frames)
        print("end get tape")
        #fileName = QFileDialog.getSaveFileName(self, "Save F:xile",
                                               #"/home/jana/untitled.png",
                                              # "Images (*.png *.xpm *.jpg)")
        #filename, _ = QFileDialog.getSaveFileName(
         #  self,
         #'',
         #"ReStructuredText Files (*.rst *.txt)"
         #)
        #fileName = QFileDialog.getOpenFileName(None, "Select a file...", './', filter="All files (*)")