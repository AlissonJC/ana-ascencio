over_50 = 0
height_average_10_20 = 0
less_40_kilos = 0

for person in range(0, 5):
    age = int(input())
    height = float(input())
    weight = float(input())

    if age > 50:
        over_50 += 1

    if 10 <= age <= 20:
        height_average_10_20 += height

    if weight < 40:
        less_40_kilos += 1

print(f"{over_50}")
print(f"{height_average_10_20 / 5}")
print(f"{less_40_kilos/5*100:.2f}%")