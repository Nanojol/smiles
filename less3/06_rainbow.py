# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# --------------------------------------------
first_pointx = 50
first_pointy = 50
# sec_pointx = 350
# sec_pointy = 450
#
# point = sd.get_point(first_pointx,first_pointy)
# sec_point = sd.get_point(sec_pointx,sec_pointy)
# for colours in rainbow_colors:
#     point = sd.get_point(first_pointx, first_pointy)
#     sec_point = sd.get_point(sec_pointx, sec_pointy)
#     first_pointx += 5
#     first_pointy += 1
#     sec_pointx += 5
#     sec_pointy += 1
#     sd.line(point, sec_point,colours,4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
rad = 50
for colours in rainbow_colors:
    rad += 50
    point = sd.get_point(300,-50)
    sd.circle(point,rad,colours,50)

sd.pause()
