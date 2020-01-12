import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<title>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_press: app.stop() 

<settings>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            
<square>:
    canvas:
        Color:
            rgba: 0, 0, 0, 0
        Line:
            width: 2.
            rectangle: (self.x, self.y, self.width, self.height)
''')

class title(Screen):
    pass

class settings(Screen):
    pass

class square(Widget):
    pass


class Screen:
    #there will be three screens: title, settings, board.

    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(title(name='menu'))
        self.sm.add_widget(settings(name='settings'))

    def get_manager(self):
        return self.sm


class Application(App):

    def build(self):
        return Screen().get_manager()

if __name__ == '__main__':
    Application().run()