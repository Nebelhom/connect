#!usr/bin/python

from __future__ import print_function

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

from levelselectgrid import LevelSelectGrid as LSG
from menu import Menu
from game import ConnectGame

Builder.load_file('menu.kv')

class ConnectApp(App):
    def build(self):
        self.parent = RelativeLayout()
        self.menu = Menu()
        self.lsg = LSG(cols=3)
        self.lvl = None
        # ConnectGame defined when self.lvl known

        self.parent.add_widget(self.menu)
        Clock.schedule_interval(self.update, 1. / 1.5)
        return self.parent

    def update(self, dt):
        if self.menu.start_lsg:
            self.parent.clear_widgets()

            # Create ScrollView around LSG
            self.scroll = ScrollView() # 4 scroll
            self.scroll.do_scroll_x = False # 4 scroll
            self.scroll.do_scroll_y = True # 4 scroll
            self.scroll.add_widget(self.lsg) # 4 scroll
            self.parent.add_widget(self.scroll) # 4 scroll

            self.menu.start_lsg = False

        elif self.lsg.lvl is not None:
            self.game = ConnectGame(lvl=self.lsg.lvl)
            self.parent.clear_widgets()
            self.parent.add_widget(self.game)
            self.lsg.lvl = None

if __name__ == '__main__':
    ConnectApp().run()