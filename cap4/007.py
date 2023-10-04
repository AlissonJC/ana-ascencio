salary = float(input())

if salary < 500:
    bonus = salary * 0.3
    new_salary = salary + bonus
    print(f"Novo salário: R${new_salary:.2f}")
else:
    print(f"Não há aumento.")