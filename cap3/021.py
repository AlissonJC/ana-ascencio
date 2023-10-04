worked_hours, minimum_salary, extra_worked_hours = map(float, input().split())

worked_hour_value = minimum_salary / 8
extra_worked_hours_value = minimum_salary / 4
gross_salary = worked_hours * worked_hour_value
extra_payment = extra_worked_hours * extra_worked_hours_value

salary = gross_salary + extra_payment

print(f"R$ {salary:.2f}")