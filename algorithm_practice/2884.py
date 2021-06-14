input_num = input().split(' ')
hour = int(input_num[0])
min = int(input_num[1])

if hour > 0 and min < 45:
    min += 60
    hour -= 1
    print(hour, min - 45)
elif hour <= 0 and min < 45:
    hour = 23
    min += 60
    print(hour, min - 45)
elif hour < 0:
    print(23, min - 45)
else:
    print(hour, min - 45)
