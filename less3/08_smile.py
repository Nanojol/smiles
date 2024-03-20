# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(cord_x, cord_y, colour):
   palitra = {
       'COLOR_RED': (255, 0, 0),
       'COLOR_ORANGE': (255, 127, 0),
       'COLOR_YELLOW': (255, 255, 0),
       'COLOR_GREEN': (0, 255, 0),
       'COLOR_CYAN': (0, 255, 255),
       'COLOR_BLUE': (0, 0, 255),
       'COLOR_PURPLE': (255, 0, 255)
   }

   point = sd.get_point(cord_x, cord_y)
   sd.circle(point, 100, palitra[colour], 5)
   eyes_left = sd.get_point(cord_x-35,cord_y+20)
   eyes_right = sd.get_point(cord_x+30,cord_y+20)
   sd.circle(eyes_left, 10, palitra[colour], 5)
   sd.circle(eyes_right, 30, palitra[colour], 5)
   mouth_point_bot = sd.get_point(cord_x-70,cord_y-80)
   mouth_point_top = sd.get_point(cord_x+20,cord_y-20)
   sd.ellipse(mouth_point_bot,mouth_point_top,palitra[colour], 0)

for _ in range(10):
    x = random.randrange(1,600)
    y = random.randrange(1,600)
    print(smile(x,y,'COLOR_YELLOW'))


sd.pause()
