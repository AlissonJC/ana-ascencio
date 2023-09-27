base_salary, years = map(float, input().split())

if base_salary < 200:
    tax = 0
elif 200 <= base_salary <= 450:
    tax = base_salary * 0.03
elif 450 < base_salary < 700:
    tax = base_salary * 0.08
else:
    tax = base_salary * 0.12

if base_salary >= 500 and years <= 3:
    bonus = 20
elif base_salary >= 500 and years > 3:
    bonus = 30
elif base_salary < 500:
    if years <= 3:
        bonus = 23
    elif 3 < years < 6:
        bonus = 35
    else:
        bonus = 33

net_salary = base_salary - tax + bonus

print(f"R${net_salary:.2f}")

if net_salary <= 350:
    print("A")
elif 350 < net_salary < 600:
    print("B")
else:
    print("C")