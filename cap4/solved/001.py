nota_trab, aval_sem, exame = map(float, input().split())

media = (nota_trab*2 + aval_sem*3 + exame*5)/10

print(f"Média ponderada: {media:.2f}")

if 8 <= media <= 10:
    print("Obteve conceito A")
elif 7 <= media < 8:
    print("Obteve conceito B")
elif 6 <= media < 7:
    print("Obteve conceito C")
elif 5 <= media < 6:
    print("Obteve conceito D")
else:
    print("Obteve conceito E")