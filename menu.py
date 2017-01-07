#!usr/bin/python

from __future__ import print_function

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import BooleanProperty, ListProperty, NumericProperty

from test import SchemeGame

# Use hexTap as orientation!!! Awesome!!!

class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        # Top Row label
        # Choose level
        # Settings -> None yet, maybe set sound later and all that, now only return
        # Exit -> Exit game d'uh
        self.start_game = False


class MenuApp(App):
    def build(self):
    	self.parent = RelativeLayout()
        self.menu = Menu()
        self.game = SchemeGame()
        self.parent.add_widget(self.menu)
        Clock.schedule_interval(self.update, 1. / 1.5)
        return self.parent

    def update(self, dt):
    	if self.menu.start_game:
			self.parent.clear_widgets()
			self.parent.add_widget(self.game)
			self.menu.start_game = False

if __name__ == '__main__':
    MenuApp().run()