price = float(input())

if price <= 30:
    discount = 0
elif 30 < price <= 100:
    discount = price * 0.1
else:
    discount = price * 0.15

new_price = price - discount

print(f"Desconto: R${discount:.2f}")
print(f"Novo preço: R${new_price:.2f}")