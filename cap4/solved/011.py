hora_i, min_i, hora_f, min_f = map(int, input().split())

if min_i > min_f:
    min_f += 60
    hora_f -= 1

if hora_i > hora_f:
    hora_f += 24

min_d = min_f - min_i
hora_d = hora_f - hora_i

print(f"O jogo durou {hora_d} horas e {min_d} minutos.")