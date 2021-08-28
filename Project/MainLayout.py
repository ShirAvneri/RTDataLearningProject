from SideMenu import *
from TopBar import *
from Content import *


class MainLayout(QWidget):
    def __init__(self, width, height, parent=None):
        super(MainLayout, self).__init__(parent)
        self.setGeometry(0, 0, width, height)
        self.side_menu = SideMenu(self)
        self.top_bar = TopBar(self)
        self.content = Content(self)

    def set_content(self, new_content):
        self.content = new_content

    def change_notes(self,notes):
        if self.content == ClassicalGuitarTuner:
            self.content = ClassicalGuitarTuner(self.content)
            self.content.change_notes(notes)
