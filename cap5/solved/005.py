terms = int(input("Digite o número de termos: "))
x = float(input("Digite um valor positivo para X: "))

den = None
s = 0
denominator = 0

for i in range(0, terms):
    end = denominator
    fat = 1
    for j in range(0, end):
        fat *= j

    power = i + 1
    if power % 2 == 0:
        s -= (x ** power)/fat
    else:
        s += (x ** power)/fat

    if denominator == 4:
        den = -1
    if denominator == 1:
        den = 1
    if den == 1:
        denominator += 1
    else:
        denominator -= 1

print(f"{s:.2f}")