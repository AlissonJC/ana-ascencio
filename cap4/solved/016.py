actual_price = float(input("Digite o preço atual do produto: "))
average_month_sale = int(input("Digite a venda média mensal: "))

if average_month_sale < 500 or actual_price < 30:
    new_price = actual_price * 1.1
elif 500 <= average_month_sale < 1200 or 30 <= actual_price < 80:
    new_price = actual_price * 1.15
elif average_month_sale >= 1200 or actual_price >= 80:
    new_price = actual_price - (actual_price * 0.2)

print(f"O novo preço do produto é de: {new_price:.2f}")