# k 광년 움직였을 때 -> k-1 , k, k+1 움직이기 가능
# 처음에는 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1만 가능
# 그 다음 0 , 1 , 2 가능 -> 1 , 2, 3
# for 문 써서 k 가 1 씩 증가하면 가능!?
#  하지만 우현이는 y 지점에 도착 시 직전의 이동거리(k) 1광년으로 하려함 ( k + 1 = 2)

test = int(input())
distance = 0
for i in range(test):
    x, y = list(map(int, input().split(' ')))
    distance = y - x  # 거리
    count = 0  # 이동 횟수
    move = 1  # count 별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance:
        count += 1
        move_plus += move
        if count % 2 == 0:  # count 가 2의 배수일 때,
            move += 1
    print(count)
# ------- 작동 방식 -------- #
# distance = 3 - 0 = 3
# count = 0
# move = 1
# move_plus = 0
# ------ while 문 -------- # 0 3 을 넣었을 때
# while 0(move_plus) < 3(distance) : True
# count = 1
# 0(move_plus) + 1(move) = 1
# 1 % 2 != 0 -> if 조건 통과못함!
# while 1(move_plus) < 3(distance): True
# count = 2
# 1(move_plus) + 1(move) = 2
# 2 % 2 == 0 -> if 조건 통과!
# move = 2
# while 2(move_plus) < 3(distance): True
# count = 3
# 2(move_plus) + 2(move) = 4
# 4 % 2 == 0 -> if 조건 통과!
# move = 3
# while 3(move_plus) < 3(distance): False!
# print(count) count = 3 이기 때문에 3이 출력됨
