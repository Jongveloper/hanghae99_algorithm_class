# O가 들어오면 처음엔 1 연속으로 들어오면 1+2+3....하다가 X가 들어오면 +0 다시 O가 들어오면 +1 + 2


n = int(input())
for i in range(n):
    a = input()
    a_list = list(a)  # a를 리스트화 시켜준다.
    cnt = 1  # O가 들어오면 처음에 들어올 때 1을 더해줘야하기 때문에 cnt의 초기 값은 1
    total = 0  # cnt 를 전부 더해준 값
    for j in a_list:
        if j == "O":  # 만약 j 가 O 면
            total += cnt  # total = cnt + 1
            cnt += 1  # cnt = cnt+1
        else:
            cnt = 1  # j 가 X 면 cnt 를 1로 초기화
    print(total)
