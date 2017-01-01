#!usr/bin/python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import BooleanProperty, ListProperty, NumericProperty

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
    collision = BooleanProperty(False)
    highlight = BooleanProperty(False)
    # Coordinates of the center of the widget
    pos_center = ListProperty([])
    def __init__(self, key, **kwargs):
        super(Dot, self).__init__(**kwargs)

        # Widget Properties
        self.size_hint = None, None
        self.size = 30, 30  # The size (see update function)

        # Dot-specific Properties
        self.key = key
        self.r = 1.0
        self.pos_center = self.get_pos_center()

        # Bindings
        self.bind(pos=self.update)
        self.bind(size=self.update)

        self.bind(r=self.update)
        self.bind(pos_center=self.update)

    def get_pos_center(self):
        return ((self.pos[0] + self.width / 2.0),
                (self.pos[1] + self.height / 2.0))

    def update(self, *args):
        """
        Updates visuals
        - Input from resizing and touch_events
        """
        self.pos_center = self.get_pos_center()

        # Redraw
        self.canvas.clear()

        with self.canvas:
            Color(self.r, 1.0, 1.0, 1.0)
            Ellipse(pos=self.pos, size=self.size)


class Ray(Widget):
    """
    rel_start :: tuple x,y :: Relative start point of line
    rel_end :: tuple x,y :: Relative end point of line
    corr :: integer :: correction value to place coords in center of the circle
    """
    def __init__(self, rel_start, rel_end, corr, **kwargs):
        super(Ray, self).__init__(**kwargs)

        self.rel_start = rel_start
        self.rel_end = rel_end
        self.corr = corr

        # Bindings
        self.bind(pos=self.update)
        self.bind(size=self.update)

    def update(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(1.0, 1.0, 1.0, 1.0)
            Line(points=[self.width * self.rel_start[0] + self.corr,
                         self.height * self.rel_start[1] + self.corr,
                         self.width * self.rel_end[0] + self.corr,
                         self.height * self.rel_end[1] + self.corr])


class SchemeGame(FloatLayout):
    def __init__(self, lvl=lvl1, **kwargs):
        super(SchemeGame, self).__init__(**kwargs)

        self.finished = False

        # Pos of previously active sphere
        self.prev_pos = (-1, -1)
        # Pos of currently active sphere
        self.cur_pos = (-1, -1)

        self.lvl = lvl

        self.check = {}
        for key, value in lvl.items():
            temp = {}
            temp['x'] = value['x']
            temp['y'] = value['y']
            temp['links'] = set()
            self.check[key] = temp

        # Managing dots
        self.dots = []  # Populated in draw_dots
        self.draw_dots(self.check)
        self.draw_lines(self.check)


    def draw_dots(self, dic):
        # Draw the ellipse widgets
        for key, value in dic.items():
            e = Dot(key, pos_hint={'x': value['x'],
                                   'y': value['y']},
                    size=(30,30))
            self.dots.append(e)
            self.add_widget(e)

    def draw_lines(self, dic):
        # draw the Ray widgets
        corr = self.dots[0].size[0] / 2 # finds center of circle
        for key, value in dic.items():
            for i in value['links']:
                start = (value['x'], value['y'])
                end = (dic[i]['x'], dic[i]['y'])
                ray = Ray(start, end, corr, pos_hint={'x': value['x'], 'y': value['y']})
                self.add_widget(ray)

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

        if self.finished:
            print("All done!")

        else:

            # Check 1
            collision = False

            key1 = None  # Filled with Dot object key
            key2 = None  # Filled with Dot object

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
                    # Save new current position
                    self.cur_pos = dot.pos_center
                    key1 = dot.key

                # Check 3
                elif dot.collision and dot.highlight:
                    pass

                # Check 4
                elif collision and not dot.collision and dot.highlight:
                    dot.r = 1.0
                    dot.highlight = False
                    # Move previous active position
                    self.prev_pos = dot.pos_center
                    key2 = dot.key

            # Here we draw a new line and add to links
            if self.cur_pos != (-1, -1) and self.prev_pos != (-1, -1) and key1 and key2:
                if key1 not in self.check[key2]['links']:
                    self.check[key2]['links'].add(key1)
                if key2 not in self.check[key1]['links']:
                    self.check[key1]['links'].add(key2)
                self.draw_lines(self.check)

            print(self.check)

            # TODO: Outsource to regular update --> Finish game...
            if self.check == self.lvl:
                self.finished = True


class SchemeApp(App):
    def build(self):
        game = SchemeGame()
        return game

if __name__ == '__main__':
    SchemeApp().run()