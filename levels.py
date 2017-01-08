#!usr/bin/python3

from __future__ import division

"""
Outlines the levels in form of dictionaries
"""

# Straight Line
lvl1 = ('Easy Start', 
	    {1: {'x':0.33333,
            'y':0.5,
            'links':{2}},
         2: {'x':0.66667,
            'y':0.5,
            'links':{1}},
         })

# Triangle
lvl2 = ('Triangle',
	    {1: {'x':0.5,
            'y':0.66667,
            'links':{2,3}},
         2: {'x':0.33333,
            'y':0.33333,
            'links':{1,3}},
         3: {'x':0.66667,
            'y':0.33333,
            'links':{1,2}},
         })

# The House of Santa Claus
lvl3 = ('House of Santa Claus',
	    {1: {'x':3 / 8,
            'y':4 / 6,
            'links':{2,3,5,4}},
         2: {'x':4 / 8,
            'y':5 / 6,
            'links':{1,3}},
         3: {'x':5 / 8,
            'y': 4 / 6,
            'links':{1,2,4,5}},
         4: {'x':5 / 8,
            'y':2 / 6,
            'links':{1,3,5}},
         5: {'x':3 / 8,
            'y':2 / 6,
            'links':{1,3,4}}
         })

# Grosser Wagen - Sternzeichen
lvl4 = ('The Plough',
	    {1: {'x':0.1,
            'y':0.66667,
            'links':{2}},
         2: {'x':0.2,
            'y':0.75,
            'links':{1,3}},
         3: {'x':0.45,
            'y':0.7,
            'links':{2,4}},
         4: {'x':0.55,
            'y':0.66667,
            'links':{3,5,7}},
         5: {'x':0.8,
            'y':0.66667,
            'links':{4,6}},
         6: {'x':0.75,
            'y':0.33333,
            'links':{5,7}},
         7: {'x':0.6,
            'y':0.33333,
            'links':{4,6}}
         })

lvls_list = (lvl1, lvl2, lvl3, lvl4)
