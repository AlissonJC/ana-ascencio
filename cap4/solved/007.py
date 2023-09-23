i = int(input("Digite 1, 2 ou 3: "))
a, b, c = map(float, input("Digite três números: ").split())

if i == 1:
    if a < b < c:
        print(f"Ordem crescente: {a}, {b}, {c}")
    elif a < c < b:
        print(f"Ordem crescente: {a}, {c}, {b}")
    elif b < a < c:
        print(f"Ordem crescente: {b}, {a}, {c}")
    elif b < c < a:
        print(f"Ordem crescente: {b}, {c}, {a}")
    elif c < a < b:
        print(f"Ordem crescente: {c}, {a}, {b}")
    elif c < b < a:
        print(f"Ordem crescente: {c}, {b}, {a}")

elif i == 2:
    if a > b > c:
        print(f"Ordem decrescente: {a}, {b}, {c}")
    elif a > c > b:
        print(f"Ordem decrescente: {a}, {c}, {b}")
    elif b > a > c:
        print(f"Ordem decrescente: {b}, {a}, {c}")
    elif b > c > a:
        print(f"Ordem decrescente: {b}, {c}, {a}")
    elif c > a > b:
        print(f"Ordem decrescente: {c}, {a}, {b}")
    elif c > b > a:
        print(f"Ordem decrescente: {c}, {b}, {a}")

elif i == 3:
    if a > b and a > c:
        print(f"Sequência: {b}, {a}, {c}")
    elif b > a and b > c:
        print(f"Sequência: {a}, {b}, {c}")
    elif c > a and c > b:
        print(f"Sequência: {a}, {c}, {b}")