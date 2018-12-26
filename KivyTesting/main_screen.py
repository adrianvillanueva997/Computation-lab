import importlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

view = Builder.load_file("MainScreenView.kv")

class MainScreen(Screen):

    def handle_event(self, instance, code, **kwargs):
        pass

    def goto_train(self):
        pass

    def goto_classify(selfs):
        pass

    def goto_help(self):
        pass
