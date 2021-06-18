# a = 1000 , b = 70 이라고 하면 노트북을 한 대 생산하는데는 총 1,070만원이 듬, 열 대 생산하는데 1,700만원이 듬
# a = 1000(고정 지출) b = 70(생산 비용) a는 고정 b *= i // c = 소비자 가
# 이 때, 손익 분기점을 구해라.

# a +(b * i)
a, b, c = map(int, input().split())

# 시간 초과
# sell = 0
# i = 0
# while True:
#     sell += 1
#     cost = a + b * sell
#     if cost > c * i:
#         i += 1
#     if cost < c * i:
#         print(i)
#         break
#     if c == 1:
#         print(-1)
#         break

if b >= c : print(-1)
else: print(a//(c-b)+1)