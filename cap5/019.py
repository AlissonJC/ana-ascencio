higher_1000 = 0
lower_200 = 0
sum_profit = 0

stock = input()
while stock != "F":
    buy = float(input())
    sell = float(input())

    profit = sell - buy

    if profit > 1000:
        higher_1000 += 1

    if profit < 200:
        lower_200 += 1
    
    sum_profit += profit
    print(f"Lucro de {stock}: R${profit:.2f}")
    stock = input()

print()
print(f"Lucro maior que R$1000: {higher_1000}")
print(f"Lucro menor que R$200: {lower_200}")
print(f"Lucro total: R${sum_profit:.2f}")