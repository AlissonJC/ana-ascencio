state_code = int(input("Digite o código do estado: "))
load_weight = float(input("Digite o peso da carga em toneladas: "))
load_code = int(input("Digite o código da carga: "))

load_kilos = load_weight * 1000

if 10 <= load_code <= 20:
    load_price = load_kilos * 100
elif 21 <= load_code <= 30:
    load_price = load_kilos * 250
else:
    load_price = load_kilos * 340

if state_code == 1:
    tax = load_price * 0.35
elif state_code == 2:
    tax = load_price * 0.25
elif state_code == 3:
    tax = load_price * 0.15
elif state_code == 4:
    tax = load_price * 0.05
else:
    tax = 0

total = load_price + tax

print(f"Peso da carga em quilos: {load_kilos:.2f}")
print(f"Preço da carga: R${load_price:.2f}")
print(f"Imposto: R${tax:.2f}")
print(f"Total: R${total:.2f}")