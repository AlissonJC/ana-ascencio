cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulos = 0
brancos = 0
total = 0

vote = int(input())
while True:
    total += 1

    if vote == 1:
        cand1 += 1
        print("Voto computado")
    elif vote == 2:
        cand2 += 1
        print("Voto computado")
    elif vote == 3:
        cand3 += 1
        print("Voto computado")
    elif vote == 4:
        cand4 += 1
        print("Voto computado")
    elif vote == 5:
        nulos += 1
    elif vote == 6:
        brancos += 1
    elif vote == 0:
        print("Votação encerrada.")
        break
    vote = int(input())
print()
print(cand1)
print(cand2)
print(cand3)
print(cand4)
print(nulos)
print(brancos)
print(f"{nulos/total*100}%")
print(f"{brancos/total*100}%")