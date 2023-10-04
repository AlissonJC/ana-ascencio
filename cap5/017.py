sentinel = 1

channel_4 = 0
channel_5 = 0
channel_7 = 0
channel_12 = 0

while sentinel:
    channel = int(input())
    people = int(input())

    if channel == 4:
        channel_4 += people
    elif channel == 5:
        channel_5 += people
    elif channel == 7:
        channel_7 += people
    elif channel == 12:
        channel_12 += people
    elif channel == 0:
        break

total = channel_4 + channel_5 + channel_7 + channel_12

print(f"{channel_4/total*100}%")
print(f"{channel_5/total*100}%")
print(f"{channel_7/total*100}%")
print(f"{channel_12/total*100}%")