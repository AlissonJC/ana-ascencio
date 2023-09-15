deposit, check_1, check_2 = map(float, input().split())

tax_1 = check_1 * 0.0038
tax_2 = check_2 * 0.0038

balance = deposit - check_1 - check_2 - tax_1 - tax_2

print(balance)