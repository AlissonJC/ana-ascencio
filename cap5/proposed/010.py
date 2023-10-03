sum_even = 0
sum_primes = 0

for n in range(10):
    number = int(input())

    if number % 2 == 0:
        sum_even += number

    flag = False
    for i in range(2, number):
        if number % i == 0:
            flag = True
            break

    if not flag:
        sum_primes += number


print(sum_even)
print(sum_primes)