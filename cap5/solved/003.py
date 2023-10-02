n = int(input())

for i in range(1, n+1):
    number = int(input())
    fat = 1
    for j in range(1, number+1):
        fat *= j
    print(f"Fatorial de {j}: {fat:.0f}")