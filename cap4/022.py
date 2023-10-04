age = int(input())
weight = float(input())

if age < 20:
    if weight <= 60:
        print(9)
    elif 60 < weight <= 90:
        print(8)
    else:
        print(7)
elif 20 <= age <= 50:
    if weight <= 60:
        print(6)
    elif 60 < weight <90:
        print(5)
    else:
        print(4)
else:
    if weight <= 60:
        print(3)
    elif 60 < weight <90:
        print(2)
    else:
        print(1)