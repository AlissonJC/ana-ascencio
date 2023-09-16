from math import floor

num = float(input())

i = floor(num)
f = num - i
a = round(num)

print(f"{i}")
print(f"{f:.2f}")
print(f"{a}")