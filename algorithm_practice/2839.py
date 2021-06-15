sugar = int(input())

cnt = 0  # 설탕을 몇 번 담았는지 나타내는 저장소

while sugar >= 0:  # 설탕을 담은 갯수가 0보다 크거나 같을 때 까지 True
    if sugar % 5 == 0:  # 만약 담아야할 설탕 갯수가 5의 배수일 경우
        cnt += sugar // 5  # 저장소에 설탕을 5로 나눈 몫을 더해줍니다.
        print(cnt)
        break
    sugar -= 3  # 만약 5의 배수가 아니라면 3을 빼주고(3의 배수)
    cnt += 1  # 저장소에 1개를 추가합니다.
else:
    print(-1)  # 3, 5 의 배수가 아니라면 -1을 출력합니다.
