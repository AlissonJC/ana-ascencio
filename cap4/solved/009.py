import datetime

now = datetime.datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute

if minute < 10:
    minute = "0"+str(minute)

if month == 1:
    month_name = "Janeiro"
elif month == 2:
    month_name = "Fevereiro"
elif month == 3:
    month_name = "Março"
elif month == 4:
    month_name = "Abril"
elif month == 5:
    month_name = "Maio"
elif month == 6:
    month_name = "Junho"
elif month == 7:
    month_name = "Julho"
elif month == 8:
    month_name = "Agosto"
elif month == 9:
    month_name = "Setembro"
elif month == 10:
    month_name = "Outubro"
elif month == 11:
    month_name = "Novembro"
else:
    month_name = "Dezembro"

print(f"Data atual: {day}/{month}/{year} - {month_name}")
print(f"Hora atual: {hour}:{minute}")