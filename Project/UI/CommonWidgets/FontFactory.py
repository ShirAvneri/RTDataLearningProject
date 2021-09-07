from PySide6.QtGui import QFont


def font_factory(font_type):
    font = QFont()
    font.setFamilies([u"Calibri"])

    if font_type == "12":
        font.setPointSize(12)
    elif font_type == "12Bold":
        font.setPointSize(12)
        font.setBold(True)
    elif font_type == "14":
        font.setPointSize(14)
    elif font_type == "14Bold":
        font.setPointSize(14)
        font.setBold(True)
    if font_type == "16":
        font.setPointSize(16)
    elif font_type == "16Bold":
        font.setPointSize(16)
        font.setBold(True)
    if font_type == "18":
        font.setPointSize(18)
    elif font_type == "18Bold":
        font.setPointSize(18)
        font.setBold(True)

    return font
