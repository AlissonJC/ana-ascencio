num_1, num_2 = map(float, input().split())

if num_1 > num_2:
    print(f"{num_1} é o maior")
elif num_2 > num_1:
    print(f"{num_2} é o maior")
else:
    print("Os números são iguais")