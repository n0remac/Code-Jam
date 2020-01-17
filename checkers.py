from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.context_instructions import Color
# Hello, this is just for practice

BLACK = (0.3, 0.3, 0.35, 1)
WHITE = (1, 1, 1, 1)

class TitleMenu(Screen):
    pass


class SettingsMenu(Screen):
    pass


class DifficultySetting(Widget):
    pass


class PlayerSetting(Widget):
    def select_players(self, player_count: int):
        if player_count > 1:
            self.ids.count.text = f"{player_count} Players Selected"
        self.ids.count.text = f"{player_count} Player Selected"


class Board(Screen):
    pass

class Square(Button):
    def __init__(self, count):
        super(Square, self).__init__()

        self.background_normal = ''
        self.background_color = BLACK if (count + count//8)%2 else WHITE

class Screen:
    # There will be three screens: title, settings, board.
    # A class that keeps track of gamestates will likely be needed.

    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(TitleMenu(name="menu"))
        self.sm.add_widget(SettingsMenu(name="settings"))
        layout = GridLayout(cols=8, rows=8)
        for i in range(64):
            layout.add_widget(Square(i))
        b = Board(name='board')
        b.add_widget(layout)
        self.sm.add_widget(b)

    def get_manager(self):
        return self.sm


class Application(App):
    def build(self):
        Builder.load_file("checkers.kv")
        return Screen().get_manager()


if __name__ == "__main__":
    Application().run()
