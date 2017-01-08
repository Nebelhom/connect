#!usr/bin/python

from __future__ import print_function

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

from levels import lvls_list



#Dynamically create scrollable grid of all levels.all

#* Get a list of all levels (how?) - TICK
#* Dynamically create a button per level (Give Title) - TICK
#* Make them dynamically set lvl and start it - TICK
#* Make it scrollable


class LvlButton(Button):
	"""
	Button Class written specifically for LevelSelectGrid (LSG)
	It must 'only' be used within LSG, otherwise references borked
	"""
	def __init__(self, key, **kwargs):
		super(LvlButton, self).__init__(**kwargs)
		self.key = key

	def on_press(self):
		self.parent.lvl = lvls_list[self.key]

class LevelSelectGrid(GridLayout):
    def __init__(self, **kwargs):
        super(LevelSelectGrid, self).__init__(**kwargs)
        self.size_hint_y = None

        self.lvl = None
        # To allow for scrolling
        self.bind(minimum_height=self.setter('height'))

        key = 0
        for lvl in lvls_list:
        	b = LvlButton(key, text=lvl[0], size_hint_y=None, height=200)
        	self.add_widget(b)
        	key += 1
