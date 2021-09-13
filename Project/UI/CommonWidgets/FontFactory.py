from PySide6.QtGui import QFont


def create_font(size=12, bold=False):
    font = QFont()
    font.setFamilies(["Calibri"])
    font.setPointSize(size)
    font.setBold(bold)
    return font
