price = float(input())

if price <= 50:
    increase = price * 0.05
elif 50 < price <= 100:
    increase = price * 0.1
else:
    increase = price * 0.15

new_price = price + increase

if new_price <= 80:
    print("Barato")
elif 80 < new_price <= 120:
    print("Normal")
elif 120 < new_price <= 200:
    print("Caro")
else:
    print("Muito caro")