product_code = int(input("Digite o código do produto: "))
product_weight = float(input("Digite o peso do produto em quilos: "))
country_code = int(input("Digite o código do país de origem: "))

total_weight = product_weight * 1000

if 1 <= product_code <= 4:
    total_price = total_weight * 10
elif 5 <= product_code <= 7:
    total_price = total_weight * 25
else:
    total_price = total_weight * 35

if country_code == 1:
    tax = 0
elif country_code == 2:
    tax = total_price * 0.15
elif country_code == 3:
    tax = total_price * 0.25

final_value = total_price + tax

print(f"Peso em gramas: {total_weight:.2f}")
print(f"Preço total do produto: {total_price:.2f}")
print(f"Valor do imposto: R${tax:.2f}")
print(f"Valor total: R${final_value:.2f}")