gross_salary = float(input())

if gross_salary <= 350:
    bonus = 100
elif 350 < gross_salary < 600:
    bonus = 75
elif 600 <= gross_salary <= 900:
    bonus = 50
else:
    bonus = 35

salary = gross_salary + bonus
tax = salary * 0.07

net_salary = salary - tax

print(f"Salário a receber: R${net_salary:.2f}")