nota_1, nota_2, nota_3 = map(float, input().split())

media = (nota_1 + nota_2 + nota_3)/3

print(f"Média Aritmética: {media:.2f}")

if 0 <= media < 3:
    print("Reprovado")
elif 3 <= media < 7:
    print("Exame")
    exame = 12 - media
    print(f"Deve tirar {exame:.2f} para ser aprovado.")
else:
    print("Aprovado")