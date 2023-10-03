average = 0
age = int(input())

average += age
amount = 1

while age:
    age = int(input())
    if age == 0:
        break
    amount += 1
    average += age

print(f"{average/amount:.2f}")