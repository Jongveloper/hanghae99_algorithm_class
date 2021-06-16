# h는 층 수 , w는 각 층의 방 수, n은 손님 수
# 각 손님은 층 수는 상관 없고 호수가 작은 걸 선호
# 만약 6층에 각 방이 12개가 있다면 10번 째 온 손님은 402호



rooms = int(input())

for i in range(rooms):
    h, w, n = map(int, input().split(' '))
    f = 0  # f 는 층 수 저장소
    ho = 0  # ho 는 호실 수 저장소
    if n % h == 0:  # n 을
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)