#!usr/bin/python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse
from kivy.properties import NumericProperty

# Kivy colors in RGBA
WHITE = Color(1.0, 1.0, 1.0, 1.0)
RED = Color(1.0, 0.0, 0.0, 1.0)
GREEN = Color(0.0, 1.0, 0.0, 1.0)
BLUE = Color(0.0, 0.0, 1.0, 1.0)
BLACK = Color(0.0, 0.0, 0.0, 1.0)


class Dot(Widget):
    def __init__(self, **kwargs):
        super(Dot, self).__init__(**kwargs)

        # Properties
        self.r = 1.0
        self.size = 30, 30

        # Bindings
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
        # In order to take effect
        self.update()

    def update(self, *args):
        """
        Updates visuals
        - Input from resizing and touch_events
        """
        # clear canvas
        self.canvas.clear()

        # Redraw canvas
        with self.canvas:
            Color(self.r, 1.0, 1.0, 1.0)
            Ellipse(pos=self.pos, size=(30, 30))

class SchemeGame(FloatLayout):
    def __init__(self,**kwargs):
        super(SchemeGame, self).__init__(**kwargs)

        # Draw the ellipse widgets
        e = Dot(pos_hint={'x': 0.5, 'y': 0.5}, size=(30,30))
        self.add_widget(e)


class SchemeApp(App):
    def build(self):
        game = SchemeGame()
        return game

if __name__ == '__main__':
    SchemeApp().run()