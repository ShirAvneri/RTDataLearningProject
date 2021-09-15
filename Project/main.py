import sys
from PySide6.QtWidgets import QApplication

from Project.Tester import Tester
from Project.UI.AppMainWindow import AppMainWindow


def main():
    # tester = Tester()
    # for i in range (20):
    #     expected_output = tester.create_test_sample(1)
    #     tester.execute_test(expected_output)
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
