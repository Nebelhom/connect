#!usr/bin/python

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout


class Menu(BoxLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        # lsg = levelselectgrid
        self.start_lsg = False
        self.start_settings = False
