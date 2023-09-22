num_1, num_2, num_3 = map(float, input().split())

if num_1 < num_2 < num_3:
    print(f"A ordem crescente é {num_1}, {num_2}, {num_3}")
elif num_1 < num_3 < num_2:
    print(f"A ordem crescente é {num_1}, {num_3}, {num_2}")
elif num_2 < num_1 < num_3:
    print(f"A ordem crescente é {num_2}, {num_1}, {num_3}")
elif num_2 < num_3 < num_1:
    print(f"A ordem crescente é {num_2}, {num_3}, {num_1}")
elif num_3 < num_1 < num_2:
    print(f"A ordem crescente é {num_3}, {num_1}, {num_2}")
elif num_3 < num_2 < num_1:
    print(f"A ordem crescente é {num_3}, {num_2}, {num_1}")