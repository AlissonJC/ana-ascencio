while True:
    print("1. Novo salário")
    print("2. Férias")
    print("3. Décimo terceiro")
    print("4. Sair")
    menu = int(input("Digite a opção desejada: "))

    print()
    if menu == 1:
        salary = float(input("Digite o salário: "))
        if salary <= 210:
            salary *= 1.15
        elif 210 < salary <= 600:
            salary *= 1.1
        else:
            salary *= 1.05
        print(f"R${salary:.2f}")
        break
    elif menu == 2:
        salary = float(input("Digite o salário: "))
        vacation = salary + (salary / 3)
        print(f"Férias: R${vacation:.2f}")
        break
    elif menu == 3:
        salary = float(input("Digite o salário: "))
        months = int(input("Digite a quantidade de meses: "))
        extra = salary * months / 12
        print(f"Décimo terceiro: R${extra:.2f}")
        break
    elif menu == 4:
        print("Finalizando programa.")
        break