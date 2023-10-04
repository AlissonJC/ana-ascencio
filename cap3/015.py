salary = float(input("Digite o salário: "))
bill_1 = float(input("Digite a primeira conta: "))
bill_2 = float(input("Digite a segunda conta: "))

bill_1 = bill_1 * 1.02
bill_2 = bill_2 * 1.02

total = salary - bill_1 - bill_2

print(f"{total:.2f}")