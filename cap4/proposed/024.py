price = float(input())
category = int(input())
frozen = input().upper()

if price <= 25:
    if category == 1:
        increase = 0.05 * price
    elif category == 2:
        increase = 0.08 * price
    elif category == 3:
        increase = 0.1 * price
elif price > 25:
    if category == 1:
        increase = 0.12 * price
    elif category == 2:
        increase = 0.15 * price
    elif category == 3:
        increase = 0.18 * price

print(f"Aumento: R${increase:.2f}")

if category == 2 or frozen == "R":
    tax = 0.05 * price
else:
    tax = 0.08 * price

print(f"Imposto: R${tax:.2f}")

new_price = price + increase + tax

print(f"Novo preço: R${new_price:.2f}")

if new_price <= 50:
    print("Barato")
elif 50 < new_price < 120:
    print("Normal")
else:
    print("Caro")