values = []

value = int(input())
while value != 0:
    if value < 0:
        print("Valor desconsiderado")
    else:
        values.append(value)
    value = int(input())

values.sort()
higher = values[-1]
lower = values[0]

print(f"Maior: {higher}")
print(f"Menor: {lower}")