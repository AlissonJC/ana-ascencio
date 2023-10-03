values = []

for value in range(0, 5):
    a, b, c, d = map(int, input().split())

    values.append(a)
    values.append(b)
    values.append(c)
    values.append(d)

    cresc = sorted(values)
    decresc = sorted(values, reverse=True)

    print(values)
    print(f"Crescente: {cresc}")
    print(f"Decrescente: {decresc}")