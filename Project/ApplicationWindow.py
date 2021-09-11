from PySide6.QtWidgets import QMainWindow

from Project.UI.ContentTypes.GuitarTuner.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.MediatorPattern import GuiMediator
from Project.UI.SideMenuTypes.GuitarTunerSideMenu import GuitarTunerSideMenu
from Project.UI.TopBar import TopBar


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setFixedSize(900, 600)
        self.setWindowTitle("CSMusic App")
        content = ClassicalGuitarTunerContent()
        side_menu = GuitarTunerSideMenu()
        top_bar = TopBar()
        self.mediator = GuiMediator(self, top_bar, side_menu, content)
