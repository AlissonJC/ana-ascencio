num_1, num_2, num_3 = map(float, input("Digite três números em ordem crscente: ").split())

num_4 = float(input("Digite um quarto número: "))

if num_4 > num_3:
    print(f"A ordem decrescente é: {num_4}, {num_3}, {num_2}, {num_1}")
elif num_2 < num_4 < num_3:
    print(f"A ordem decrescente é: {num_3}, {num_4}, {num_2}, {num_1}")
elif num_1 < num_4 < num_2:
    print(f"A ordem decrescente é: {num_3}, {num_2}, {num_4}, {num_1}")
elif num_4 < num_1:
    print(f"A ordem decrescente é: {num_3}, {num_2}, {num_1}, {num_4}")