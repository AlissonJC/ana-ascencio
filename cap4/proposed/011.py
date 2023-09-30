salary = float(input())

if salary <= 300:
    increase = salary * 0.15
elif 300 < salary < 600:
    increase = salary * 0.1
elif 600 <= salary <= 900:
    increase = salary * 0.05
else:
    increase = 0

print(f"Aumento: R${increase:.2f}")
print(f"Novo salário: R${salary:.2f}")