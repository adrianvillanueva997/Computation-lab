import importlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import main_screen


class MainApp(App):

    screen_manager = ObjectProperty(Builder.load_file("main_view.kv"))
    window_stack = ListProperty()

    def build(self):
        self.screen_manager.add_widget(main_screen.MainScreen())

        #Build the paths here
        return self.screen_manager



if __name__ == '__main__':
    MainApp().run()

