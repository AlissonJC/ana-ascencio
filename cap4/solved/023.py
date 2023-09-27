minimum_salary = float(input())
shift = input()
category = input()
worked_hours = int(input())

if shift == 'M':
    coef = minimum_salary * 0.1
elif shift == 'V':
    coef = minimum_salary * 0.15
else:
    coef = minimum_salary * 0.12
    
print(f"Coeficiente: {coef:.2f}")

gross_salary = worked_hours * coef

print(f"Salário Bruto: R${gross_salary:.2f}")

if category == 'O':
    if gross_salary >= 300:
        tax = gross_salary * 0.05
    else:
        tax = gross_salary * 0.03
else:
    if gross_salary >= 400:
        tax = gross_salary * 0.06
    else:
        tax = gross_salary * 0.04

print(f"Imposto: R${tax:.2f}")

if shift == 'N' and worked_hours > 80:
    bonus = 50
else:
    bonus = 30

if category == 'G' or coef <= 25:
    food = gross_salary / 3
else:
    food = gross_salary / 2

print(f"Auxílio alimentação: R${food:.2f}")

net_salary = gross_salary - tax + bonus + food

print(f"Salário líquido: R${net_salary:.2f}")

if net_salary < 350:
    print("Mal remunerado")
elif 350 <= net_salary <= 600:
    print("Normal")
else:
    print("Bem remunerado")