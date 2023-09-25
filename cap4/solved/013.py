print("Menu de opções: ")
print("1. Imposto")
print("2. Novo salário")
print("3. Classificação")
menu = int(input("Digite a opção desejada: "))

if menu == 1:
    salary = float(input("Digite o salário: "))
    if salary < 500:
        tax = salary * 0.05
        print(f"Imposto: R$ {tax:.2f}")
    elif 500 <= salary <= 850:
        tax = salary * 0.1
        print(f"Imposto: R$ {tax:.2f}")
    else:
        tax = salary * 0.15
        print(f"Imposto: R$ {tax:.2f}")
elif menu == 2:
    salary = float(input("Digite o salário: "))
    if salary > 1500:
        salary += 25
        print(f"O novo salário é: R$ {salary:.2f}")
    elif 750 <= salary <= 1500:
        salary += 50
        print(f"O novo salário é: R$ {salary:.2f}")
    elif 450 <= salary < 750:
        salary += 75
        print(f"O novo salário é: R$ {salary:.2f}")
    else:
        salary += 100
        print(f"O novo salário é: R$ {salary:.2f}")
elif menu == 3:
    salary = float(input("Digite o salário: "))
    if salary <= 700:
        print("Mal remunerado")
    else:
        print("Bem remunerado")