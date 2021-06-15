n = int(input())
cnt = 0  # 영화 개봉 횟수 1탄 : 666 , 2탄 : 1666 , ..... 9666 , 6661, 6662
title = 666  # 무조건 포함되어 있어야하는 제목
while True:
    if '666' in str(title):  # 만약 title 에 666 이 있다면
        cnt += 1  # cnt 를 + 1 해줍니다.
    if cnt == n:  # cnt 와 n 이 같다면
        print(title)  # 출력
        break  # 멈춥니다.
    title += 1  # cnt != n 이라면 title 을 + 1 해줍니다.
221

