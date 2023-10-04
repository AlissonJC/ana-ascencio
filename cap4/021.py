price = float(input())
code = int(input())

if code == 1:
    print("Sul")
elif code == 2:
    print("Norte")
elif code == 3:
    print("Leste")
elif code == 4:
    print("Oeste")
elif code == 5 or code == 6:
    print("Nordeste")
elif 7 <= code <= 9:
    print("Sudeste")
elif 10 <= code <= 20:
    print("Centro-oeste")
elif 21 <= code <= 30:
    print("Nordeste")