cost = 200
sales = 120
ticket = 5
profit = (ticket * sales) - cost
print(f"Lucro: R${profit:.2f}")
print(f"Vendas: R${sales:.2f}")
print(f"Preço: R${ticket}")

while ticket > 1:
    ticket -= 0.5
    sales += 26
    profit = (ticket * sales) - cost
    print()
    print(f"Lucro: R${profit:.2f}")
    print(f"Vendas: R${sales:.2f}")
    print(f"Preço: R${ticket}")

