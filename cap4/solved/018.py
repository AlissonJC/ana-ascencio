x, y, z = map(float, input("Digite três valores para os lados do triângulo: ").split())

if x < (y + z) and y < (x + z) and z < (x + y):
    if x == y == z:
        print("Equilátero")
    elif x == y or x == z or y == z:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Valores não formam um triângulo.")