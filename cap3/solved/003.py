g1, g2, g3, w1, w2, w3 = map(float, input().split())

average = (g1*w1 + g2*w2 + g3*w3)/(w1+w2+w3)

print(average)