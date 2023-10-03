ages = 0
amount1 = 0
height_190 = 0
age_10_30 = 0

for person in range(10):
    age = int(input())
    weight = float(input())
    height = float(input())

    if weight > 90 and height < 1.5:
        amount1 += 1

    if height > 1.90:
        height_190 += 1
        if 10 <= age < 30:
            age_10_30 += 1

print(f"{ages/10:.2f}")
print(f"{amount1}")
print(f"{age_10_30 / height_190*100:.2f}%")