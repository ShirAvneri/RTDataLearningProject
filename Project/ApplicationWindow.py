from PySide6.QtWidgets import QMainWindow
from Project.UI.MainLayout import MainLayout


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setFixedSize(900, 600)
        self.setWindowTitle("Music Project")
        self.main_layout = MainLayout(900, 600)
        self.main_layout.setParent(self)
        self.main_layout.init_layout()
        self.setCentralWidget(self.main_layout)

