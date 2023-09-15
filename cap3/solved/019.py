height_step, height_ladder = map(float, input().split())

amount_step = height_ladder / height_step

print(f"{amount_step:.0f}")