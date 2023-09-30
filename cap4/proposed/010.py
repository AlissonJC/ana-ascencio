cost = float(input())

if cost <= 12000:
    dist = cost * 0.05
    tax = 0
elif 12000 < cost <= 25000:
    dist = cost * 0.1
    tax = cost * 0.15
else:
    dist = cost * 0.15
    tax = cost * 0.2

final = cost + dist + tax

print(f"Preço final: R${final:.2f}")