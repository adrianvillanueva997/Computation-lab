import importlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

view = Builder.load_file("main_screen_view.kv")

class MainScreen(Screen):

    def handle_event(self, instance, key, **kwargs):
        if key == "TRAIN":
            self.goto_train()
        elif key == "CLASSIFY":
            self.goto_classify()
        elif key == "HELP":
            self.goto_help()

    def goto_train(self):
        print("TODO: Implement goto_train")
        pass

    def goto_classify(selfs):
        print("TODO: Implement goto_classify")
        pass

    def goto_help(self):
        print("TODO: Implement goto_help")
        pass

