lenght, width = map(float, input().split())

area = lenght * width

light_power = area * 18

print(f"Área: {area:.2f} metros quadrados")
print(f"Potência Necessária: {light_power:.2f}W")