a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Estes valores não formam uma equação do segundo grau.")
else:
    delta = b**2 - (4 * a * c)
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        print("Existe uma raiz real.")
        x = -b/(2*a)
        print(f"X = {x:.2f}")
    else:
        print("Existem duas raízes reais.")
        x1 = (-b + (delta ** (1 / 2))) / (2 * a)
        x2 = (-b - (delta ** (1 / 2))) / (2 * a)