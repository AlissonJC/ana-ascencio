n = int(input())

amount = 0

for i in range(2, n+1):
    if n % i == 0:
        amount += 1

if amount > 2:
    print("Número não-primo")
else:
    print("Número primo")