import os
import sys

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

from Project.Constants import OS_PATH
from Project.UI.AppMainWindow import AppMainWindow


def main():
    # tester = Tester()
    # for i in range (20):
    #     expected_output = tester.create_test_sample(1)
    #     tester.execute_test(expected_output)
    app = QApplication(sys.argv)
    fonts_path = os.path.join(OS_PATH, 'UI', 'Fonts')
    for font_dir in ['Open Sans']:
        for font in filter(lambda s: s.endswith('.ttf'), os.listdir(os.path.join(fonts_path, font_dir))):
            QFontDatabase.addApplicationFont(os.path.join(fonts_path, font_dir, font))
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
