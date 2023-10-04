faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

average1 = 0
average2 = 0
average3 = 0
average4 = 0

for person in range(15):
    age = int(input())
    weight = float(input())

    if 1 <= age <= 10:
        faixa1 += 1
        average1 += weight
    elif 11 <= age <= 20:
        faixa2 += 1
        average2 += weight
    elif 21 <= age <= 30:
        faixa3 += 1
        average3 += weight
    else:
        faixa4 += 1
        average4 += weight

print(f"{faixa1/average1:.2f}")
print(f"{faixa2/average2:.2f}")
print(f"{faixa3/average3:.2f}")
print(f"{faixa4/average4:.2f}")