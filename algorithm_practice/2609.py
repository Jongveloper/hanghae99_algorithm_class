# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수 구하기
# 문제 접근 방식 :
# 최대공약수: a 와 b의 최대공약수는 b 와 a를 나눈 나머지의 최대공약수와 같다.
# 최소공배수: a 와 b의 최소공배수는 a*b/최대공약수(a,b)를 해주면 최수 공배수가 된다.
# 최소공배수가 되는 이유는 이 수를 a와 b 모두 나누어떨어지고 나누어 떨어지는 수 중 가장 작은 수이기 때문이다.

l, r = map(int, input().split(' '))


def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(l, r))
print(lcm(l, r))
