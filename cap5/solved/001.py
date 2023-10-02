current_year = int(input())

salary = 1000
increase = 0.015
new_salary = salary * (1+increase)

for year in range(2007, current_year):
    increase *= 2
    new_salary = salary * (1+increase)

print(f"O novo salário é de: R${new_salary:.2f}")