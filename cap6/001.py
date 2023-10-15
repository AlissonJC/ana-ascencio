n = []

for i in range(6):
    x = int(input())
    n.append(x)

print("Pares")
count_even = 0
for i in range(len(n)):
    if n[i] % 2 == 0:
        count_even += 1
        print(n[i])
print(f"Quantidade de pares: {count_even}")

print("Ímpares")
count_odd = 0
for i in range(len(n)):
    if n[i] % 2 != 0:
        count_odd += 1
        print(n[i])
print(f"Quantidade de ímpares: {count_odd}")