#!usr/bin/python

import os

"""
texture = Image('mycombinedimage.png').texture

bottomleft = texture.get_region(0, 0, 64, 64)
bottomright = texture.get_region(0, 64, 64, 64)
topleft = texture.get_region(0, 64, 64, 64)
topright = texture.get_region(64, 64, 64, 64)
"""

ROOT = os.getcwd()

"""
starry =

width=370, height=390

star1 = 90, 95, 460, 485
star2 = 90, 465, 460, 855
star3 = 90, 855, 460, 1245

star4 = 460, 95, 550, 485
star5 = 460, 465, 550, 855
star6 = 460, 855, 550, 1245

star7 = 830, 95, 920, 485
star8 = 830, 465, 920, 855
star9 = 830, 855, 920, 1245
"""

star_path = os.path.join(ROOT, 'imgs', 'starry_sky')
star_img = os.path.join(star_path, 'star1.png')

stars = [os.path.join(star_path, 'star1.png'),
         os.path.join(star_path, 'star2.png'),
         os.path.join(star_path, 'star3.png'),
         os.path.join(star_path, 'star4.png'),
         os.path.join(star_path, 'star3.png'),
         os.path.join(star_path, 'star2.png'),
         os.path.join(star_path, 'star1.png')]

starry_bg = os.path.join(star_path, 'background.jpg')

starry = {'bg': starry_bg,
		  'spritesheet': star_img, 
		  'dots': stars}