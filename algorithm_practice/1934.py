# 유클리드 호제법을 사용하자
# a를 b로 나눈 나머지를 r 이라 했을 때 a와 b의 최대 공약수는 b와 r의 최대공약수
# 최소 공배수 : gcd * a를 gcd 에 나눴을 때의 몫 * b를 gcd 에 나눴을 때의 몫

def gcd(a, b):  # 최대 공약수 재귀 함수 구현
    return gcd(b % a, a) if b % a else a


def lcm(a, b):  # 최소 공배수
    c = gcd(a, b)
    return c * (a // c) * (b // c)


n = int(input())
for i in range(n):
    left, right = map(int, input().split())
    print(lcm(left, right))
