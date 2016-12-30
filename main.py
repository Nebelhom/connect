#!usr/bin/python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse
from kivy.properties import BooleanProperty, NumericProperty

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

class TouchException(Exception):
    print("An expected combination of factors were observed.")

class Dot(Widget):
    r = NumericProperty(0)
    collision = BooleanProperty(False)
    highlight = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(Dot, self).__init__(**kwargs)

        # Widget Properties
        self.size_hint = None, None
        self.size = 30, 30  # The size (see update function)

        # Dot-specific Properties
        self.r = 1.0

        # Bindings
        self.bind(pos=self.update)
        self.bind(size=self.update)

        self.bind(r=self.update)

    def update(self, *args):
        """
        Updates visuals
        - Input from resizing and touch_events
        """

        # Redraw
        self.canvas.clear()

        with self.canvas:
            Color(self.r, 1.0, 1.0, 1.0)
            Ellipse(pos=self.pos, size=self.size)


class SchemeGame(FloatLayout):
    def __init__(self,**kwargs):
        super(SchemeGame, self).__init__(**kwargs)

        # Managing dots
        self.dots = []

        # Draw the ellipse widgets
        for key, value in lvl1.items():
            e = Dot(pos_hint={'x': value['x'], 'y': value['y']}, size=(30,30))
            self.dots.append(e)
            self.add_widget(e)

    def on_touch_down(self, touch):
        """
        The function does the following checks:

        Check 1: Is a sphere clicked?
        Check 2: Is the clicked sphere the active sphere?
                If not, make it active
        Check 3: If already active -> pass
        Check 4: Trickiest one of the lot:
                We need to know if
                    * There was a collision with a different sphere -> collision
                    * The collision was not with this sphere -> not dot.collision
                    * The sphere was previously highlighted -> dot.highlighted
        """

        # Check 1
        collision = False

        for dot in self.dots:
            if dot.collide_point(*touch.pos):
                dot.collision = True
                collision = True
            else:
                dot.collision = False

        for dot in self.dots:
            # Check 2
            if dot.collision and not dot.highlight:
                dot.r = 0.0
                dot.highlight = True
            # Check 3
            elif dot.collision and dot.highlight:
                pass
            # Check 4
            elif collision and not dot.collision and dot.highlight:
                dot.r = 1.0
                dot.highlight = False




class SchemeApp(App):
    def build(self):
        game = SchemeGame()
        return game

if __name__ == '__main__':
    SchemeApp().run()