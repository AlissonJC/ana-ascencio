d1, m1, a1 = map(int, input("Digite três números para representar a primeira data: ").split())

d2, m2, a2 = map(int, input("Digite três números para representar a segunda data: ").split())

if a1 > a2:
    print(f"A data maior é: {d1}/{m1}/{a1}")
elif a1 < a2:
    print(f"A data maior é: {d2}/{m2}/{a2}")
else:
    if m1 > m2:
        print(f"A data maior é: {d1}/{m1}/{a1}")
    elif m1 < m2:
        print(f"A data maior é: {d2}/{m2}/{a2}")
    else:
        if d1 > d2:
            print(f"A data maior é: {d1}/{m1}/{a1}")
        elif d1 < d2:
            print(f"A data maior é: {d2}/{m2}/{a2}")
        else:
            print("As datas são iguais.")