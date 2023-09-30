height = float(input())
gender = input().upper()

if gender == "M":
    weight = 72.7 * height - 58
else:
    weight = 62.1 * height - 44.7

print(f"Peso ideal: {weight:.2f}kg")