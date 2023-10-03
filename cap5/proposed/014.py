great_age_average = 0
greate_amount = 0

regular_amount = 0

good_amount = 0

for viewer in range(15):
    age = int(input())
    rate = int(input())

    if rate == 3:
        great_age_average += age
        greate_amount += 1

    if rate == 1:
        regular_amount += 1

    if rate == 2:
        good_amount += 1

print(great_age_average/greate_amount)
print(regular_amount)
print(f"{good_amount/15*100:.2f}%")