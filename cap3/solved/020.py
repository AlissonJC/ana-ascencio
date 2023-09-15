from math import sin

angle, height_ladder = map(float, input().split())

radian = angle * 3.14 / 180

ladder = height_ladder / sin(radian)