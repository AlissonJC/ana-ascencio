x, y = map(float, input().split())

if x > y:
    print(f"{x:.2f} é o maior")
elif x < y:
    print(f"{y:.2f} é o maior")
else:
    print("Os números são iguais")