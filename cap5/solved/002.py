n = int(input())

e = 1

for i in range(1, n):
    fat = 1
    for j in range(1, i+1):
        fat *= j
    e += 1/fat

print(f"{e:.2f}")