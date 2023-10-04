faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for person in range(0, 8):
    age = int(input())

    if age <= 15:
        faixa1 += 1
    elif 16 <= age <= 30:
        faixa2 += 1
    elif 31 <= age <= 45:
        faixa3 += 1
    elif 46 <= age <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

print(f"Faixa 1: {faixa1}")
print(f"Faixa 2: {faixa2}")
print(f"Faixa 3: {faixa3}")
print(f"Faixa 4: {faixa4}")
print(f"Faixa 5: {faixa5}")
print(f"Porcentagem da primeira faixa: {faixa1 / 8*100:.2f}%")
print(f"Porcentagem da última faixa: {faixa5 / 8*100:.2f}%")