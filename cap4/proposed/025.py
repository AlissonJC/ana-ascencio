extra_hours = int(input())
missed_hours = int(input())

hours_in_minutes = (extra_hours - (2 / 3 * missed_hours)) * 60

if hours_in_minutes >= 2400:
    bonus = 500
elif 1800 < hours_in_minutes < 2400:
    bonus = 400
elif 1200 <= hours_in_minutes < 1800:
    bonus = 300
elif 600 <= hours_in_minutes < 1200:
    bonus = 200
else:
    bonus = 100

print(f"Bônus: R${bonus:.2f}")