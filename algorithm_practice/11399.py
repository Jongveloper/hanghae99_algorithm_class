# 은행에 atm 이 1대 밖에 없다
# 첫째 줄엔 대기 인원 수
# 둘째 줄엔 대기 인원의 돈 뽑는 시간
n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)