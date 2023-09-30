angle = float(input())

if angle > 360 or angle < -360:
    turn = angle // 360
    angle = angle % 360
else:
    turn = 0

if angle == 0 or angle == 90 or angle == 180 or angle == 270 or angle == 360 \
        or angle == -90 or angle == -180 or angle == -270 or angle == -360:
    print("O ângulo está em cima de algum dos eixos.")
elif 0 < angle < 90 or -270 > angle > -360:
    print("Primeiro quadrante")
elif 90 < angle < 180 or -180 > angle > -270:
    print("Segundo quadrante")
elif 180 < angle < 270 or -90 > angle > -180:
    print("Terceiro quadrante")
elif 270 < angle < 360 or 0 > angle > -90:
    print("Quarto quadrante")

print(f"{turn} voltas.")

if angle < 0:
    print("Sentido horário")
else:
    print("Sentido anti-horário")

print(angle)