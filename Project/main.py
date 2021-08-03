import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainLayout import *


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setFixedSize(900, 600)
    window.setWindowTitle("Music Project")
    MainLayout(900, 600, window)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
