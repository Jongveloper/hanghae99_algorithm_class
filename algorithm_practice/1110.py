input_num = int(input())
num = input_num
cnt = 0
while True:
    ten_num = num // 10  # 10의 자리수 반환 : 2 6 8 4
    one_num = num % 10  # 1의 자리수 반환 : 6 8 4 2
    sum_num = (ten_num + one_num) % 10  # 10의 자리 + 1의 자리를 더하고 10으로 나눈 나머지 반환
    # 8 4 2 6
    num = (one_num * 10) + sum_num  # 1의 자리에 10을 곱한 후 sum_num 을 더한 값을 반환:
    # 68 84 42 26
    cnt += 1  # 1 2 3 4
    if num == input_num:  # False False False
        break

print(cnt)
