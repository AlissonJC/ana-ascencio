birth = int(input("Digite o ano de nascimento: "))
actual = int(input("Digite o ano atual: "))

years = actual - birth
months = years * 12
days = years * 365
weeks = years * 52

print(years)
print(months)
print(days)
print(weeks)