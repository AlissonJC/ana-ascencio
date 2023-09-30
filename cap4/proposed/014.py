salary = float(input())

if salary <= 300:
    increase = salary * 0.5
elif 300 < salary <= 500:
    increase = salary * 0.4
elif 500 < salary <= 700:
    increase = salary * 0.3
elif 700 < salary <= 800:
    increase = salary * 0.2
elif 800 < salary <= 1000:
    increase = salary * 0.1
else:
    increase = salary * 0.05

new_salary = salary + increase

print(f"Novo salário: R${new_salary:.2f}")