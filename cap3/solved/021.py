from math import sin

ladder, height_picture = map(float, input().split())

distance = (height_picture**2 - ladder**2)**1/2

print(f"{distance:.2f}")