from PySide6.QtGui import QFont

from Project.UI.ContentTypes.ChordDetection.ChordDetectionContent import ChordDetectionContent
from Project.UI.ContentTypes.GuitarTuner.AcousticGuitarTunerContent import AcousticGuitarTunerContent
from Project.UI.ContentTypes.GuitarTuner.ClassicalGuitarTunerContent import ClassicalGuitarTunerContent
from Project.UI.ContentTypes.GuitarTuner.ElectricGuitarTunerContent import ElectricGuitarTunerContent
from Project.UI.ContentTypes.Metronome.MetronomeContent import MetronomeContent
from Project.UI.ContentTypes.Music.MusicContent import MusicContent
from Project.UI.ContentTypes.Recording.RecordingContent import RecordingContent
from Project.UI.ContentTypes.SongUpload.SongUploadContent import SongUploadContent
from Project.UI.Enums import AppWidgetTypes
from Project.UI.SideMenuComponent import SideMenu
from Project.UI.SideMenuTypes.GuitarTunerSideMenu import GuitarTunerSideMenu
from Project.UI.SideMenuTypes.MetronomeSideMenu import MetronomeSideMenu
from Project.UI.TopBarComponent import TopBar


class Factory:
    @staticmethod
    def create_content(content_type: AppWidgetTypes):
        return ContentFactory.content_factory(content_type)

    @staticmethod
    def create_side_menu(side_menu_type: AppWidgetTypes):
        return SideMenuFactory.side_menu_factory(side_menu_type)

    @staticmethod
    def create_top_bar():
        return TopBarFactory.top_bar_factory()


class ContentFactory:
    @staticmethod
    def content_factory(of_type=AppWidgetTypes.CONTENT):
        if of_type == AppWidgetTypes.CLASSIC_TUNER_CONTENT:
            return ClassicalGuitarTunerContent()
        if of_type == AppWidgetTypes.ELECTRIC_TUNER_CONTENT:
            return ElectricGuitarTunerContent()
        if of_type == AppWidgetTypes.ACOUSTIC_TUNER_CONTENT:
            return AcousticGuitarTunerContent()
        if of_type == AppWidgetTypes.RECORDING_CONTENT:
            return RecordingContent(True)
        if of_type == AppWidgetTypes.CHORD_DETECTION_CONTENT:
            return ChordDetectionContent(True)
        if of_type == AppWidgetTypes.METRONOME_CONTENT:
            return MetronomeContent()
        if of_type == AppWidgetTypes.UPLOAD_CONTENT:
            return SongUploadContent(True)
        if of_type == AppWidgetTypes.MUSIC_CONTENT:
            return MusicContent(True)

        return None


class SideMenuFactory:
    @staticmethod
    def side_menu_factory(of_type: AppWidgetTypes):
        if of_type == AppWidgetTypes.SIDE_MENU:
            return SideMenu()
        if of_type == AppWidgetTypes.TUNER_SIDE_MENU:
            return GuitarTunerSideMenu()
        if of_type == AppWidgetTypes.METRONOME_SIDE_MENU:
            return MetronomeSideMenu()

        return None


class TopBarFactory:
    @staticmethod
    def top_bar_factory():
        return TopBar()
