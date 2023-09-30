x, y, z = map(float, input().split())

if x > y and x > z:
    print(f"{x:.2f} é o maior")
elif y > x and y > z:
    print(f"{y:.2f} é o maior")
elif z > x and z > y:
    print(f"{z:.2f} é o maior")
elif x == y == z:
    print("Os números são iguais")