age = int(input())

if age < 5:
    print("Fora de categoria")
elif 5 <= age <= 7:
    print("Infantil")
elif 8 <= age <= 10:
    print("Juvenil")
elif 11 <= age <= 15:
    print("Adolescente")
elif 16 <= age <= 30:
    print("Adulto")
else:
    print("Sênior")