from math import cos

angle, distance = map(float, input().split())

radian = angle * 3.1415 / 180

ladder = distance / cos(radian)

print(f"Altura: {ladder:.2f}")