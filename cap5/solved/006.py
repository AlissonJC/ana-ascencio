for worker in range(0,10):
    code = int(input("Digite o código do funcionário: "))
    worked_hours = int(input("Digite o número de horas trabalhadas: "))
    shift = input("Digite o turno: ")
    category = input("Digite a categoria: ")
    minimum_salary = 450

    if category == "G" and shift == "N":
        worked_hour_value = minimum_salary * 0.18
    elif category == "G" and shift == "M" or shift == "V":
        worked_hour_value = minimum_salary * 0.15
    elif category == "O" and shift == "N":
        worked_hour_value = minimum_salary * 0.13
    elif category == "O" and shift == "M" or shift == "V":
        worked_hour_value = minimum_salary * 0.1

    salary = worked_hours * worked_hour_value

    if salary <= 300:
        food = salary * 0.2
    elif 300 < salary <= 600:
        food = salary * 0.15
    else:
        food = salary * 0.05

    final_salary = salary + food

    print(f"Funcionário: {code}")
    print(f"Horas trabalhadas: {worked_hours}")
    print(f"Salário inicial: R${salary:.2f}")
    print(f"Auxílio alimentação: R${food:.2f}")
    print(f"Salário final: R${final_salary:.2f}")
    print()