amount = 0

for n in range(10):
    number = int(input())

    flag = False
    for i in range(2, number):
        if number % i == 0:
            flag = True
            break

    if not flag:
        amount += 1

print(amount)