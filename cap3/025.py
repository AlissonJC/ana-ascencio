hour, minutes = map(int, input().split())

hour_in_minutes = hour * 60
total_minutes = hour_in_minutes + minutes
seconds = total_minutes * 60

print(f"Hora em minutos: {hour_in_minutes}")
print(f"Total de minutos: {total_minutes}")
print(f"Total em segundos: {seconds}")