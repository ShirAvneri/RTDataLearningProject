import sys
from PySide6.QtWidgets import QApplication
from Project.ApplicationWindow import ApplicationWindow


def main():
    app = QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
