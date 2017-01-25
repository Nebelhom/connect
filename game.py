#!usr/bin/python

from __future__ import print_function

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
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

class Touch_Widget(Widget):
    def __init__(self, **kwargs):
        super(Touch_Widget, self).__init__(**kwargs)

        # Widget Properties
        self.size_hint = None, None

        # Bindings
        self.bind(pos=self.update)
        self.bind(size=self.update)

    def update(self, *args):
        self.pos
        self.size

class Dot(Widget):
    """
    r :: float :: value of red in Color
    highlight :: bool :: True if currently active sphere
    perc :: float :: percentage of window width, used to create size of spheres
    template :: bool :: Decides if sphere is clickable or not and if in self.dots or not

    """
    r = NumericProperty(0)
    highlight = BooleanProperty(False)
    def __init__(self, key, template=False, **kwargs):
        super(Dot, self).__init__(**kwargs)

        # Widget Properties
        self.size_hint = None, None

        # Dot-specific Properties
        self.key = key
        self.r = 1.0

        # Bindings
        self.bind(pos=self.update)
        self.bind(size=self.update)

        self.bind(r=self.update)
        self.bind(highlight=self.update)

    def update(self, *args):
        """
        Updates visuals
        - Input from resizing and touch_events
        """

        if self.highlight:
            self.r = 0.0
        else:
            self.r = 1.0

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


class ConnectGame(FloatLayout):
    def __init__(self, lvl=lvl1, **kwargs):
        super(ConnectGame, self).__init__(**kwargs)

        # Check if game is finished
        self.finished = False
        # Check if player wants to exit
        self.exit = False
        # Check if player wants to go back to levelselect
        self.levelselect = False

        self.lvl = lvl[1]

        self.check = {}
        for key, value in lvl[1].items():
            temp = {}
            temp['x'] = value['x']
            temp['y'] = value['y']
            temp['links'] = set()
            self.check[key] = temp

        # Managing dots
        self.dots = {}  # Populated in draw_dots
        self.active_dot = 0  # Key of active dot

        # Managing lines
        self.rays = []

        # Template
        self.draw_dots(self.lvl, template=True, perc=0.05, rel_pos=0.2)
        corr_temp = (self.width * 0.05) / 2
        self.draw_lines(self.lvl, corr_temp, rel_pos=0.2, template=True)

        # Game
        self.draw_dots(self.check)
        self.corr = self.dots[1].size[0] / 2
        self.draw_lines(self.check, self.corr)

        # Add Buttons
        self.exitBtn = Label(text="Exit", size_hint=(0.075, 0.075), pos_hint={'right': 1, 'top': 0.075})
        self.levelselectBtn = Label(text="Level\nselect", size_hint=(0.075, 0.075), pos_hint={'right': 1 - 0.075 - 0.01, 'top': 0.075})
        self.resetBtn = Label(text="Reset", size_hint=(0.075, 0.075), pos_hint={'right': 1 - 0.15 - 0.02, 'top': 0.075})
        self.add_widget(self.exitBtn)
        self.add_widget(self.levelselectBtn)
        self.add_widget(self.resetBtn)

        # Widget to check for touch pos
        # Size allows for some margin of error in touching
        dia = self.width * 0.4
        self.t_widget = Touch_Widget(size_hint=(None, None), size=(10, 10), pos=(0,0))

        # Congratulations message at the end
        txt = "Congratulations!"
        self.congrats = Label(text=txt, size_hint=(None, None), font_size=70,
                              pos_hint={'center':(0.5, 0.7)})

    def draw_dots(self, dic, template=False, perc=0.4, rel_pos=1.0):
        """
        dic :: dict :: information on circle
        perc :: float :: size of circle relative to parent width
        rel_pos :: float :: positional adjust based on percentage
        """
        # diameter of circle
        diam = self.width * perc
        # Draw the ellipse widgets
        for key, value in dic.items():
            e = Dot(key, template,
                    pos_hint={'x': value['x'] * rel_pos,
                              'y': value['y'] * rel_pos},
                    size=[diam, diam])
            self.add_widget(e)
            # If template, it should not be in the checked list
            if not template:
                self.dots[key] = e

    def draw_lines(self, dic, corr, rel_pos=1.0, template=False):
        """
        Draw the Ray widgets

        dic :: dict :: information on lines
        corr :: float :: correction factor to find center of the circe
        rel_pos :: float :: ositional adjust based on percentage
        """

        # To allow for function reset to work
        if not template:
            for ray in self.rays:
                self.remove_widget(ray)
            self.rays = []

        for key, value in dic.items():
            for i in value['links']:
                start = (value['x'] * rel_pos, value['y'] * rel_pos)
                end = (dic[i]['x'] * rel_pos, dic[i]['y'] * rel_pos)
                ray = Ray(start, end, corr, pos_hint={'x': value['x'],
                                                      'y': value['y']})
                self.add_widget(ray)

                if not template:
                    self.rays.append(ray)

    def reset(self):
        # Reset all values
        self.finished = False
        for item in self.check.items():
            item[1]['links'] = set()
        self.remove_widget(self.congrats)

        if self.active_dot != 0:
            self.dots[self.active_dot].highlight = False
            self.active_dot = 0

        # Remove all lines from the game
        self.draw_lines(self.check, self.corr)

    def on_touch_down(self, touch):

        # Touch widget positioned at touch and add
        self.t_widget.x = touch.x - (self.t_widget.width / 2)
        self.t_widget.y = touch.y - (self.t_widget.width / 2)
        self.add_widget(self.t_widget)

        # Avoid error from adding widget when finished
        self.remove_widget(self.congrats)

        if self.finished:
            self.add_widget(self.congrats)

        if self.resetBtn.collide_widget(self.t_widget):
            self.reset()

        if self.exitBtn.collide_widget(self.t_widget):
            self.exit = True

        if self.levelselectBtn.collide_widget(self.t_widget):
            self.levelselect = True

            # TODO: Outsource to regular update --> Finish game...
            if self.check == self.lvl:
                self.finished = True

        # Remove touch widget again
        self.remove_widget(self.t_widget)


    def on_touch_move(self, touch):
        """
        The function does the following checks:

        Check 1: Is a sphere clicked?
        Check 2: Is the clicked sphere the active sphere?
                If not, make it active -> STILL TODO unless connection already exists
                STILL TODO: if already exists, make aware (print out for now, later a probably sound)
        Check 3: If already active -> pass
        Check 4: Trickiest one of the lot:
        """

        # Touch widget positioned at touch and add
        self.t_widget.x = touch.x - (self.t_widget.width / 2)
        self.t_widget.y = touch.y - (self.t_widget.width / 2)
        self.add_widget(self.t_widget)

        # Avoid error from adding widget when finished
        self.remove_widget(self.congrats)

        # Used in else loop below
        new_dot = 0

        if self.finished:
            self.add_widget(self.congrats)

        """
        if self.resetBtn.collide_widget(self.t_widget):
            self.reset()

        if self.exitBtn.collide_widget(self.t_widget):
            self.exit = True

        if self.levelselectBtn.collide_widget(self.t_widget):
            self.levelselect = True
        """

        # If active dot not set yet
        if self.active_dot == 0:
            for key, dot in self.dots.items():
                if dot.collide_widget(self.t_widget):
                    dot.highlight = True
                    self.active_dot = key

        # There is an active dot already set
        else:
            for key, dot in self.dots.items():
                if dot.collide_widget(self.t_widget):
                    # Clicking the same dot
                    if key == self.active_dot:
                        # TODO: exchange for buzz sound
                        print('Same Dot!')
                    else:
                        new_dot = key

            # New circle clicked and link does not exist yet            
            if new_dot != 0 and \
               new_dot not in self.check[self.active_dot]['links']:
                # Create new links
                self.check[new_dot]['links'].add(self.active_dot)
                self.check[self.active_dot]['links'].add(new_dot)
                self.draw_lines(self.check, self.corr)

                # Change highlighting
                self.dots[new_dot].highlight = True
                self.dots[self.active_dot].highlight = False
                self.active_dot = new_dot
            # Either clicking same circle -> caught above
            # Or clicking first circle of the game -> no error!
            elif new_dot == 0:
                pass
            else:
                print("Link already exists!!!!")

            # TODO: Outsource to regular update --> Finish game...
            if self.check == self.lvl:
                self.finished = True

        # Remove touch widget again
        self.remove_widget(self.t_widget)
