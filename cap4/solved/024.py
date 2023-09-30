price = float(input())
product_type = input().upper()
frozen = input().upper()

if frozen == "N":
    if product_type == "A":
        if price < 15:
            extra = 2
        else:
            extra = 5
    elif product_type == "L":
        if price < 10:
            extra = 1.50
        else:
            extra = 2.50
    else:
        if price < 30:
            extra = 3
        else:
            extra = 2.50
else:
    if product_type == "A":
        extra = 8
    else:
        extra = 0

print(f"Valor adicional: R${extra:.2f}")

if price < 25:
    tax = price * 0.05
else:
    tax = price * 0.08

cost = price + tax
print(f"Preço de custo: {cost:.2f}")

if product_type != "A" and frozen != "S":
    discount = cost * 0.03
else:
    discount = 0
print(f"Desconto: R${discount:.2f}")

final_price = cost - discount
print(f"Preço final: R${final_price:.2f}")

if final_price <= 50:
    print("Barato")
elif 50 < final_price < 100:
    print("Normal")
else:
    print("Caro")