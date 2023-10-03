yes = 0
no = 0

women_yes = 0
men_no = 0

men = 0

for person in range(10):
    gender = input()
    answer = input()

    if answer == "S":
        yes += 1
    elif answer == "N":
        no += 1

    if answer == "S" and gender == "F":
        women_yes += 1

    if answer == "N" and gender == "M":
        men_no += 1

    if gender == "M":
        men += 1

print(yes)
print(no)
print(women_yes)
print(f"{men_no/men*100:.2f}%")