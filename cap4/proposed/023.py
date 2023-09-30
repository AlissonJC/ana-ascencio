code = int(input())
amount = int(input())

recipe = 0

if 1 <= code <= 10:
    recipe = 10 * amount
    print("Preço: R$10,00")
    print(f"Nota: R$ {recipe:.2f}")
elif 11 <= code <= 20:
    recipe = 15 * amount
    print("Preço: R$15,00")
    print(f"Nota: R$ {recipe:.2f}")
elif 21 <= code <= 30:
    recipe = 20 * amount
    print("Preço: R$20,00")
    print(f"Nota: R$ {recipe:.2f}")
elif 31 <= code <= 40:
    recipe = 30 * amount
    print("Preço: R$30,00")
    print(f"Nota: R$ {recipe:.2f}")

if recipe <= 250:
    discount = recipe * 0.05
    recipe -= discount
    print(f"Desconto: R${discount:.2f}")
    print(f"Preço final: R${recipe:.2f}")
elif 250 < recipe <= 500:
    discount = recipe * 0.1
    recipe -= discount
    print(f"Desconto: R${discount:.2f}")
    print(f"Preço final: R${recipe:.2f}")
else:
    discount = recipe * 0.15
    recipe -= discount
    print(f"Desconto: R${discount:.2f}")
    print(f"Preço final: R${recipe:.2f}")