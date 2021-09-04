import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Project.UI.ContentTypes.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.MainLayout import MainLayout


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setFixedSize(900, 600)
    window.setWindowTitle("Music Project")
    layout = MainLayout(900, 600, window)
    layout.set_content(ClassicalGuitarTunerContent(window))
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
