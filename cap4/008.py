salary = float(input())

if salary <= 300:
    salary *= 1.35
else:
    salary *= 1.15

print(f"Novo salário: R${salary:.2f}")