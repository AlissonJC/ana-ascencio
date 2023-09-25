salary = float(input("Digite o salário: "))

if salary <= 500:
    bonus = salary * 0.05
elif 500 < salary <= 1200:
    bonus = salary * 0.12
else:
    bonus = 0

if salary <= 600:
    scolarship = 150
else:
    scolarship = 100

print(f"O novo salário é de R$ {salary + bonus + scolarship:.2f}")