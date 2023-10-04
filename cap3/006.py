salary, sales = map(float, input().split())

comission = sales * 0.04

final = salary + comission

print(f"{final:.2f}")