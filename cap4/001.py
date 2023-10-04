n1, n2, n3, n4 = map(float, input().split())

average = (n1+n2+n3+n4)/4

if average >= 7:
    print("Aprovado")
else:
    print("Reprovado")