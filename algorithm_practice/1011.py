# k 광년 움직였을 때 -> k-1 , k, k+1 움직이기 가능
# 처음에는 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1만 가능
# 그 다음 0 , 1 , 2 가능 -> 1 , 2, 3
# for 문 써서 k 가 1 씩 증가하면 가능!?
#  하지만 우현이는 y 지점에 도착 시 직전의 이동거리(k) 1광년으로 하려함 ( k + 1 = 2)

test = int(input())
distance = 0
for i in range(test):
    x, y = list(map(int, input().split(' ')))
    # fast_move = x + 1
    # move = x
    # while True:
    #     if x <= 0:
    #         distance += 1
    #         x += 1
    #     if y - x >= y - x + 1:
    #         fast_move
    #     if y - x <= y - x + 1:
    #         move
    #     if y == 0:
    #         print(distance)
    #     break
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