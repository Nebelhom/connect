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
