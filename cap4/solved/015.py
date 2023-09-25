minimum_salary = float(input("Digite o valor do salário mínimo: "))
worked_hours = int(input("Digite a quantidade de horas trabalhadas: "))
childs = int(input("Digite a quantidade de dependentes: "))
extra_hours = int(input("Digite a quantidade de horas extras trabalhadas: "))

worked_hour_value = minimum_salary/5
extra_hour_value = (worked_hour_value * 1.5) * extra_hours
gross_salary = worked_hours * worked_hour_value + childs * 32 + extra_hour_value

if gross_salary < 200:
    irrf = 0
elif 200 <= gross_salary <= 500:
    irrf = gross_salary * 0.1
else:
    irrf = gross_salary * 0.2

net_salary = gross_salary - irrf

if net_salary <= 350:
    bonus = 100
else:
    bonus = 50

print(f"O salário a receber é de R$ {net_salary+bonus:.2f}")