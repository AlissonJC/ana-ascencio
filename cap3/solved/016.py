worked_hours, minimum_wage = map(float, input().split())

worked_hour_value = minimum_wage/2
salary = worked_hour_value * worked_hours
tax = salary * 0.03
final_salary = salary - tax

print(final_salary)