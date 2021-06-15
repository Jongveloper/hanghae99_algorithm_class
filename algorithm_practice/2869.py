# 시간 초과...
# a, b, v = map(int, input().split(' '))
# day = 0
# location = 0
#
# while True:
#     day += 1  # 1 2 3
#     if location < v:  # T T T T
#         location = a + location  # 2 3 4 6
#         if location >= v:  # F F F T
#             print(day)
#             break
#         location = location - b  # 1 2 3 5

# 달팽이는 하루에 a - b 만큼 움직입니다.
# 하지만 목표지점에 도달했을 때는 미끄러지지 않기 때문에 v - b 만큼 올라갑니다.
# v - b 에 a - b를 나누었을 때 나머지가 0이 아니라면
# 하루가 더 필요하므로 몫에 1을 더해주고
# 나머지가 0이라면 몫을 출력합니다.
a, b, v = map(int, input().split(' '))
day = 0
if (v - b) % (a - b) != 0:
    day = ((v - b) // (a - b)) + 1
else:
    day = ((v - b) // (a - b))
print(day)