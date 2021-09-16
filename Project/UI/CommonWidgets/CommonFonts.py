from PySide6.QtGui import QFont


def create_font(size=10, bold=False):
    font = QFont(["Open Sans"])
    font.setPointSize(size)
    font.setBold(bold)
    return font
