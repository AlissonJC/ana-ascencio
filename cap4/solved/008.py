print("Menu de opções: ")
print("1. Somar dois números.")
print("2. Raiz quadrada de um número.")

menu = int(input("Digite uma opção: "))

if menu == 1:
    a, b = map(float, input("Digite os dois números para soma: ").split())
    soma = a + b
    print(f"Soma: {soma:.2f}")

elif menu == 2:
    a = float(input("Digite o número para calcular a raiz quadrada: "))
    raiz = a**(1/2)
    print(f"A raiz quadrada de {a:.2f} é: {raiz:.2f}")
else:
    print("Opção inválida.")