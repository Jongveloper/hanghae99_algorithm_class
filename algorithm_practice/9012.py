# 괄호를 문자열로 입력받아 한쌍의 괄호로 이루어지면 YES 를 출력 아니면 NO


n = int(input())

for i in range(n):
    s = input()
    s_list = list(s)  # 두번째 줄에 입력되는 input 을 리스트형태로 형변환
    s_sum = 0
    for i in s_list:
        if i == '(':
            s_sum += 1  # ( 괄호가 나오면 s_sum 에 1을 더해준다.
        elif i == ')':
            s_sum -= 1  # ) 괄호가 나오면 s_sum 에 1을 빼준다.
        if s_sum < 0:  # 만약 s_sum 이 -1이 되면 No 를 출력하고 for 문을 빠져나온다.
            print('NO')
            break
    if s_sum > 0:  # s_sum 이 0보다 크다면 NO를 출력
        print('NO')
    elif s_sum == 0:  # s_sum 이 0이라면 YES 를 출력
        print('YES')
