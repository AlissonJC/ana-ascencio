n = int(input("Digite o número de termos: "))

num1 = 2
num2 = 7
num3 = 3
print(num1)
print(num2)
print(num3)

i = 4
while i <= n:
    num1 *= 2
    print(num1)
    i += 1
    if i <= n:
        num2 *= 3
        print(num2)
        i += 1
        if i <= n:
            num3 *= 4
            print(num3)
            i += 1