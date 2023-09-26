height = float(input("Digite a altura: "))
weight = float(input("Digite o peso: "))

if height < 1.20 and weight <= 60:
    print("A")
elif height < 1.20 and 60 < weight <= 90:
    print("D")
elif height < 1.20 and weight > 90:
    print("G")
elif 1.20 <= height <= 1.70 and weight < 60:
    print("B")
elif 1.20 <= height <= 1.70 and 60 <= weight <= 90:
    print("E")
elif 1.20 <= height <= 1.70 and weight > 90:
    print("H")
elif height < 1.7 and weight < 60:
    print("C")
elif height < 1.7 and 60 <= weight <= 90:
    print("F")
elif height < 1.7 and weight > 90:
    print("I")