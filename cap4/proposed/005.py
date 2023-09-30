x, y = map(float, input().split())
menu = int(input())

if menu == 1:
    average = (x+y)/2
    print(f"Média: {average:.2f}")
elif menu == 2:
    if x > y:
        diff = x - y
    elif x < y:
        diff = y - x
    else:
        diff = 0
    print(f"Diferença: {diff:.2f}")
elif menu == 3:
    product = x * y
    print(f"Produto: {product:.2f}")
elif menu == 4:
    if y == 0:
        print("Não é possível divisão por zero.")
    else:
        division = x / y
        print(f"Divisão: {division:.2f}")
else:
    print(f"Opção inválida.")