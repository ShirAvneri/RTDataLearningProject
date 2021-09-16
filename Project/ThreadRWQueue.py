from threading import Lock

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PySide6.QtCore import QObject, QThread
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton


class ProtectedList(object):
    """ Simple queue to share data between Threads with lock protection.
        Standard buffer length is only 8! """

    def __init__(self, buffer_size=8):
        self.elements = []
        self.buffer_size = buffer_size
        self.lock = Lock()

    def put(self, element):
        self.lock.acquire()

        # append new element at the end of the list
        self.elements.append(element)

        # delete oldest element if list is too long
        if len(self.elements) > self.buffer_size:
            self.elements.pop(0)

        self.lock.release()

    def get(self):
        self.lock.acquire()

        # check if something is in the list
        if len(self.elements) > 0:
            element = self.elements[0]
            del self.elements[0]

        # if list is empty return None
        else:
            element = None

        self.lock.release()
        return element

    def __repr__(self):
        self.lock.acquire()

        string = str(self.elements)

        self.lock.release()
        return string


# The new Stream Object which replaces the default stream associated with sys.stdout
# This object just puts data in a queue!
class WriteStream(object):
    def __init__(self, queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)


# A QObject (to be run in a QThread) which sits waiting for data to come through a Queue.Queue().
# It blocks until data is available, and once it has got something from the queue, it sends
# it to the "MainThread" by emitting a Qt Signal
class MyReceiver(QObject):
    my_signal = pyqtSignal(str)

    def __init__(self, queue, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        self.queue = queue

    @pyqtSlot()
    def run(self):
        while True:
            text = self.queue.get()
            self.my_signal.emit(text)


# An example QObject (to be run in a QThread) which outputs information with print
class LongRunningThing(QObject):
    @pyqtSlot()
    def run(self):
        for i in range(1000):
            print(i)


# An Example application QWidget containing the textedit to redirect stdout to
class MyApp(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.long_running_thing = LongRunningThing()
        self.thread = QThread()
        self.layout = QVBoxLayout(self)
        self.textedit = QTextEdit()
        self.button = QPushButton('start long running thread')
        self.button.clicked.connect(self.start_thread)
        self.layout.addWidget(self.textedit)
        self.layout.addWidget(self.button)

    @pyqtSlot(str)
    def append_text(self, text):
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText(text)

    @pyqtSlot()
    def start_thread(self):
        self.long_running_thing.moveToThread(self.thread)
        self.thread.started.connect(self.long_running_thing.run)
        self.thread.start()
