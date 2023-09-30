n1, n2 = map(float, input().split())

average = (n1+n2)/2

if average >= 7:
    print("Aprovado")
elif 3 <= average < 7:
    print("Exame")
else:
    print("Reprovado")