average = 0
total = 0

age = int(input())
while age > 0:
    height = float(input())

    if age > 50:
        total += 1
        average += height

    age = int(input())


print(f"Média: {average/total:.2f}")