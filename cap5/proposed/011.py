price = float(input())

interest = 0

discount =  (price * 0.2)

print(f"Preço final: R${price - discount:.2f} à vista.")

for installment in range(6, 66, 6):
    interest += 3
    final_price = price * (1+interest/100)
    print(f"Preço final: R${final_price:.2f} em {installment} parcelas de R${final_price/installment:.2f}.")
