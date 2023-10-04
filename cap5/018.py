average_salary = 0
lowest_age = 0
highest_age = 0
women_200 = 0
lowest_salary = 0
lowest_salary_age = 0
lowest_salary_gender = ""

count = 0
while True:
    age = int(input("Idade: "))
    if age < 0:
        break
    gender = input("Gênero: ")
    salary = float(input("Salário: "))

    average_salary += salary

    if gender == "F" and salary <= 200:
        women_200 += 1

    if count == 0:
        highest_age = age
        lowest_age = age
        lowest_salary = salary
        lowest_salary_age = age
        lowest_salary_gender = gender
    else:
        if age > highest_age:
            highest_age = age
        if age < lowest_age:
            lowest_age = age
        if salary < lowest_salary:
            lowest_salary = salary
            lowest_salary_age = age
            lowest_salary_gender = gender
    count += 1

average_salary /= count
print()
print(f"Média dos salários do grupo: R${average_salary:.2f}")
print(f"Maior idade do grupo: {highest_age}")
print(f"Menor idade do grupo: {lowest_age}")
print(f"Quantidade de mulheres com salário até R$200: {women_200}")
print(f"Idade e sexo da pessoa com menor salário: {lowest_salary_age} | {lowest_salary_gender}")