while True:
    print("1. Média artimética")
    print("2. Média ponderada")
    print("3. Sair")
    menu = int(input("Digite a opção desejada: "))

    if menu == 1:
        print()
        a, b = map(float, input().split())

        average = (a + b) / 2

        print()
        print(f"Média: {average:.2f}")
        break
    elif menu == 2:
        a, b, c = map(float, input().split())
        w1, w2, w3 = map(float, (input().split()))

        average = (a * w1 + b * w2 + c * w3)/(w1 + w2+ w3)

        print()
        print(f"Média: {average:.2f}")
        break
    elif menu == 3:
        print("Finalizando programa.")
        break
    else:
        print("Opção inválida")
        break