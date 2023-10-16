n = []

for i in range(7):
    x = int(input())
    n.append(x)

for i in range(len(n)):
    if n[i] % 2 == 0:
        print(f"Múltiplo de 2: {n[i]}")

for i in range(len(n)):
    if n[i] % 3 == 0:
        print(f"Múltiplo de 3: {n[i]}")

for i in range(len(n)):
    if n[i] % 2 == 0 and n[i] % 3 == 0:
        print(f"Múltiplo de 2 e de 3: {n[i]}")