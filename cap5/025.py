code = int(input())
total = 0
total_profit = 0

while code > 0:
    category = int(input())
    value = float(input())
    total += value

    if category == 1:
        interest = 0.015
    elif category == 2:
        interest = 0.02
    elif category == 3:
        interest = 0.04

    profit = value * interest
    total_profit += profit

    code = int(input())

print(f"Total investido: R${total:.2f}")
print(f"Total de juros pagos: R${total_profit:.2f}")