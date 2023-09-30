x, y = map(float, input().split())
menu = int(input())

if menu == 1:
    print(f"x elevado a y: {x**y:.2f}")
elif menu == 2:
    print(f"Raiz quadrada de x: {x ** (1 / 2):.2f}")
    print(f"Raiz quadrada de y: {y ** (1 / 2):.2f}")
elif menu == 3:
    print(f"Raiz cúbica de x: {x ** (1 / 3):.2f}")
    print(f"Raiz cúbica de y: {y ** (1 / 3):.2f}")
else:
    print("Opção inválida")