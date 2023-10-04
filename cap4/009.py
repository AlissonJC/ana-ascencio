balance = float(input())

if balance > 400:
    credit = balance * 0.3
elif 300 < balance <= 400:
    credit = balance * 0.25
elif 200 < balance <= 300:
    credit = balance * 0.2
else:
    credit = balance * 0.1

print(f"Crédito disponível: R${credit:.2f}")