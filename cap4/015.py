investment = int(input())
value = float(input())

if investment == 1:
    final = value * 1.03
elif investment == 2:
    final = value * 1.04

print(f"Valor corrigido: R${final:.2f}")