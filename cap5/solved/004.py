car_sum = 0
accident_sum = 0
accident_count = 0
higher = 0
lower = 0
higher_city = 0
lower_city = 0

for city in range(1, 6):
    code = int(input("Digite o código da cidade: "))
    car_amount = int(input("Digite a quantidade de veículos: "))
    accident_amount = int(input("Digite a quantidade de acidentes: "))
    print()
    if city == 1:
        higher = accident_amount
        lower = accident_amount
        higher_city = code
        lower_city = code
    else:
        if accident_amount > higher:
            higher = accident_amount
            higher_city = code
        if accident_amount < lower:
            lower = accident_amount
            lower_city = code
    car_sum += car_amount
    if car_amount < 2000:
        accident_sum += accident_amount
        accident_count += 1

print(f"Cidade com mais acidentes registrados: {higher_city} com {higher} acidentes")
print(f"Cidade com menos acidentes registrados: {lower_city} com {lower} acidentes")

car_average = car_sum/5

print(f"Média de veículos: {car_average:.2f}")

if accident_count == 0:
    print("Não há cidades com menos de 2 mil carros")
else:
    accident_average = accident_sum/accident_count
    print(f"Média de acidentes em cidades com menos de 2000 carros: {accident_average:.2f}")