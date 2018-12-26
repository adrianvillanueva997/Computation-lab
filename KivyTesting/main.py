import importlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import MainScreenController

class ClassifierMainApp(App):

    screen_manager = ObjectProperty(ScreenManager())

    def build(self):
        self.screen_manager.add_widget(Screen(name="screen test"))
        #Build the paths here
        return self.screen_manager


def main():
    application = ClassifierMainApp()
    application.run()
    print(MainScreenController.test())


if __name__ == '__main__':
    main()

