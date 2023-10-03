payroll = 0
total_pieces = 0
man_made_pieces = 0
woman_made_pieces = 0
men = 0
women = 0
highest_pay = 0
highest_code = 0

for worker in range(0, 4):
    code = int(input("Digite o código: "))
    pieces = int(input("Digite a quantidade de peças: "))
    gender = input("Digite o gênero: ")
    salary = 1000

    total_pieces += pieces

    if pieces < 30:
        extra = 0
    elif 30 < pieces <= 50:
        extra = salary * 0.03 * (pieces - 30)
    else:
        extra = salary * 0.05 * (pieces - 30)

    total_salary = salary + extra
    payroll += total_salary

    if total_salary > highest_pay:
        highest_pay = total_salary
        highest_code = code


    if gender == "M":
        man_made_pieces += pieces
        men =+ 1
    elif gender == "F":
        woman_made_pieces += pieces
        women += 1

    print()
    print(f"Operário {code} | R${total_salary:.2f}")
    print()

print()
print(f"Total da folha de pagamento: R${payroll:.2f}")
print(f"Total de peças: {total_pieces}")
print(f"Média de peças feitas por homens: {man_made_pieces / men:.2f}")
print(f"Média de peças feitas por mulheres: {woman_made_pieces / women:.2f}")
print(f"Operário de maior salário: {highest_code}")
print()