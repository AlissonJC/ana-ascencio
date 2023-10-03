under_18 = 0
height_average = 0
over_80_kilos = 0

for team in range(0,5):
    for player in range(0, 11):
        age_average = 0
        age = int(input())
        weight = float(input())
        height = float(input())

        age_average += age

        if age < 18:
            under_18 += 1

        height_average += height

        if weight > 80:
            over_80_kilos += weight

        print(f"Média das idades: {age_average / 11:.2f}")


print(f"Quantidade de jogadores menores que 18 anos: {under_18}")
print(f"Média das alturas do campeoanto: {height_average:.2f}")
print(f"Porcentagem de jogadores com mais de 80kg: {over_80_kilos / 55 * 100}:.2f")