bag_weight, cat1_food, cat2_food = map(float, input().split())

cat1_food /= 1000
cat2_food /= 1000

final = bag_weight - 5 * (cat1_food + cat2_food)

print(f"{final:.2f} kg")