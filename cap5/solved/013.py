kids = int(input("Digite o número de crianças: "))

m = 0
f = 0
less_24 = 0

for kid in range(0, kids):
    gender = input("Digite o gênero: ")
    life_time = int(input("Digite o tempo de vida em meses: "))

    if gender == "M":
        m += 1
    elif gender == "F":
        f += 1

    if life_time < 24:
        less_24 += 1

print(f"Crianças do sexo feminino: {f / kids*100:.2f}%")
print(f"Crianças do sexo masculino: {m / kids*100:.2f}%")
print(f"Crianças que viveram menos de 24 meses: {less_24 / kids*100:.2f}%")