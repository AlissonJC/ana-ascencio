job = int(input("Digite um número de 1 a 5 para o cargo: "))
salary = float(input("Digite o salário: "))

if job == 1:
    print("O cargo é Escriturário")
    print(f"O valor do aumento é de R${salary * 0.5}")
    salary *= 1.50
    print(f"O novo salário é de R${salary:.2f}")
elif job == 2:
    print("O cargo é Secretário")
    print(f"O valor do aumento é de R${salary * 0.35}")
    salary *= 1.35
    print(f"O novo salário é de R${salary:.2f}")
elif job == 3:
    print("O cargo é Caixa")
    print(f"O valor do aumento é de R${salary * 0.2}")
    salary *= 1.20
    print(f"O novo salário é de R${salary:.2f}")
elif job == 4:
    print("O cargo é Gerente")
    print(f"O valor do aumento é de R${salary * 0.1}")
    salary *= 1.10
    print(f"O novo salário é de R$ {salary:.2f}")
elif job == 5:
    print("O cargo é Diretor")
    print(f"Não tem aumento.")