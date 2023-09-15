minimum_salary, kww_consumed = map(float, input().split())

value_kww = minimum_salary/5
bill = value_kww * kww_consumed
discount = bill * 0.15

total = bill - discount

print(f"{value_kww:.2f}")
print(f"{bill:.2f}")
print(f"{total:.2f}")