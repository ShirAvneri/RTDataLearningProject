from PySide6.QtGui import QFont


class Factory:
    @staticmethod
    def create_content(content_type=""):
        return ContentFactory.content_factory(content_type)

    @staticmethod
    def create_side_menu(side_menu_type=""):
        return SideMenuFactory.side_menu_factory(side_menu_type)

    @staticmethod
    def create_top_bar(top_bar_type=""):
        return TopBarFactory.top_bar_factory(top_bar_type)

    @staticmethod
    def create_font(size=12, bold=False):
        font = QFont()
        font.setFamilies(["Calibri"])
        font.setPointSize(size)
        font.setBold(bold)
        return font


class ContentFactory:
    @staticmethod
    def content_factory(of_type=""):
        pass


class SideMenuFactory:
    @staticmethod
    def side_menu_factory(of_type=""):
        pass


class TopBarFactory:
    @staticmethod
    def top_bar_factory(of_type=""):
        pass



