import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivymd.uix.boxlayout import MDBoxLayout

from kivy.properties import StringProperty


Window.size = (320,600)


class WindowManager(ScreenManager):
    """The Screens Manager"""

class MessageScreen(Screen):
    """The Home Page"""

class StoryWithImage(MDBoxLayout):
    """"""

    text = StringProperty()
    source = StringProperty()


class MainApp(MDApp):
    def build(self):
        #Setting theme properties
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_color_palette = "Teal"
        self.theme_cls_accent_hue = 400

        self.title = "WhatsApp 2.0"

        #Screens List
        screens = [
            MessageScreen(name='message')
        ]

        self.window_manager = WindowManager(transition=FadeTransition())
        for screen in screens:
            self.window_manager.add_widget(screen)

        return self.window_manager

if __name__ == "__main__":
    MainApp().run()
