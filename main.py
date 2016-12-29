#!usr/bin/python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse
from kivy.properties import NumericProperty

from levels import *

"""
Help for pos_hint

coordinate always corresponds to bottom left corner of widget

'x':0 -> x = 0
'x':1 -> x = width, i.e. widget exactly outside
'x':0.5 -> x = width / 2
"""

# Kivy colors in RGBA
WHITE = Color(1.0, 1.0, 1.0, 1.0)
RED = Color(1.0, 0.0, 0.0, 1.0)
GREEN = Color(0.0, 1.0, 0.0, 1.0)
BLUE = Color(0.0, 0.0, 1.0, 1.0)
BLACK = Color(0.0, 0.0, 0.0, 1.0)

class Dot(Widget):
    r = NumericProperty(0)
    def __init__(self, **kwargs):
        super(Dot, self).__init__(**kwargs)

        # Properties
        self.r = 1.0
        self.size_hint = None, None
        self.size = 30, 30  # The size (see update function)

        # Bindings
        self.bind(r=self.update)
        self.bind(pos=self.update)
        self.bind(size=self.update)

    def on_touch_down(self, touch):
        """
        Checks if mouse clicks on Widget
        If so, it changes color
        """
        if self.collide_point(*touch.pos):
            if self.r > 0.0:
                self.r = 0.0
            else:
                self.r = 1.0

    def update(self, *args):
        """
        Updates visuals
        - Input from resizing and touch_events
        """
        self.canvas.clear()

        with self.canvas:
            Color(self.r, 1.0, 1.0, 1.0)
            Ellipse(pos=self.pos, size=self.size)


class SchemeGame(FloatLayout):
    def __init__(self,**kwargs):
        super(SchemeGame, self).__init__(**kwargs)

        # Draw the ellipse widgets
        for key, value in lvl1.items():
            e = Dot(pos_hint={'x': value['x'], 'y': value['y']}, size=(30,30))
            self.add_widget(e)

class SchemeApp(App):
    def build(self):
        game = SchemeGame()
        return game

if __name__ == '__main__':
    SchemeApp().run()