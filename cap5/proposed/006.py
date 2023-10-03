prazo = 0
vista = 0

for sale in range(0, 15):
    code = int(input())
    price = float(input())

    if code == "V":
        vista += price
    elif code == "P":
        prazo += price


total = vista + prazo
prestacao = prazo / 3

print(f"{vista:.2f}")
print(f"{prazo:.2f}")
print(f"{total:.2f}")
print(f"{prestacao:.2f}")