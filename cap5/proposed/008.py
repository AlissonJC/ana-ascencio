age_over_50_weight_less_60 = 0
average_age = 0
blue = 0
ginger = 0

for person in range(0, 6):
    age = int(input())
    height = float(input())
    weight = float(input())
    eyes = input()
    hair = input()

    if age > 50 and weight < 60:
        age_over_50_weight_less_60 += 1

    if height < 1.5:
        average_age += age

    if eyes == "A":
        blue += 1

    if hair == "R" and eyes != "A":
        ginger += 1

print(f"{age_over_50_weight_less_60}")
print(f"{average_age / 6:.2f}")
print(f"{blue/6*100:.2f}%")
print(f"{ginger}")