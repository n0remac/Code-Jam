import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


class title(Screen):
    pass


class settings(Screen):
    pass


class DifficultySetting(Widget):
    pass


class PlayerSetting(Widget):
    pass


class square(Widget):
    pass


class Screen:
    #There will be three screens: title, settings, board.
    #A class that keeps track of gamestates will likely be needed.

    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(title(name='menu'))
        self.sm.add_widget(settings(name='settings'))

    def get_manager(self):
        return self.sm


class Application(App):
    def build(self):
        Builder.load_file('checkers.kv')
        return Screen().get_manager()


if __name__ == '__main__':
    Application().run()
