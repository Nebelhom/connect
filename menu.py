#!usr/bin/python

from __future__ import print_function

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import BooleanProperty, ListProperty, NumericProperty


class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        # Top Row label
        # Choose level
        # Settings -> None yet, maybe set sound later and all that, now only return
        # Exit -> Exit game d'uh

        # Use kv language for that


class MenuApp(App):
    def build(self):
        menu = Menu()
        return menu

if __name__ == '__main__':
    MenuApp().run()