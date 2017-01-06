#!usr/bin/python3

"""
Outlines the levels in form of dictionaries
"""

lvl1 = {1: {'x':0.5,
            'y':0.66667,
            'links':{2,3}},
        2: {'x':0.33333,
            'y':0.33333,
            'links':{1,3}},
        3: {'x':0.66667,
            'y':0.33333,
            'links':{1,2}},
        }

# Grosser Wagen - Sternzeichen
lvl2 = {1: {'x':0.1,
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
        }
