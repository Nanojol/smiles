# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x = 0
y = 0
for _ in range(10):
    down_point = sd.get_point(x,y)
    upper_point = sd.get_point(x+100,y+50)
    sd.rectangle(down_point, upper_point, (127, 63, 0),8)
    for count in range(7):
        down_point = sd.get_point(x, y)
        upper_point = sd.get_point(x + 100, y + 50)
        x += 100
        sd.rectangle(down_point, upper_point, (127, 63, 0), 8)
    x = -50
    y += 50
    down_point = sd.get_point(x, y)
    upper_point = sd.get_point(x + 100, y + 50)
    sd.rectangle(down_point, upper_point, (127, 63, 0), 8)
    for count in range(7):
        down_point = sd.get_point(x, y)
        upper_point = sd.get_point(x + 100, y + 50)
        x += 100
        sd.rectangle(down_point, upper_point, (127, 63, 0), 8)
    x = 0
    y += 50




sd.pause()
