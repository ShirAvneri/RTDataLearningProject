from __future__ import annotations
from abc import ABC
from Project.UI.Enums import *


class Mediator(ABC):
    def notify(self, event, *args) -> None:
        pass


class GuiMediator(Mediator):
    def __init__(self, app, top_bar, side_menu, content):
        self.app = app
        self.top_bar_component = top_bar
        self.top_bar_component.mediator = self
        self.side_menu_component = side_menu
        self.side_menu_component.mediator = self
        self.content_component = content
        self.content_component.mediator = self

    def notify(self, signal, *args) -> None:
        if isinstance(signal, SideMenuEvents):
            if signal == SideMenuEvents.CHANGE_TUNING:
                self.content_component.change_notes(args[0])
            if signal == SideMenuEvents.CHANGE_GENRE:
                self.content_component.set_min_max(args[0][0], args[0][1])
        if isinstance(signal, TunerSignals):
            self.app.change_tuner(signal)
            self.content_component = self.app.content
            self.content_component.mediator = self
        if isinstance(signal, TopBarSignals):
            self.app.change_app_functionality(signal)
            self.content_component = self.app.content
            self.content_component.mediator = self
            self.side_menu_component = self.app.side_menu
            if self.side_menu_component is not None:
                self.side_menu_component.mediator = self

