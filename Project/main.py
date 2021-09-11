import sys
from PySide6.QtWidgets import QApplication
from Project.UI.AppMainWindow import AppMainWindow


def main():
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
