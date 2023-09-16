from math import floor

hour = float(input())

h = floor(hour)
m = hour - h

conversion = h*60 + m*100

print(conversion)