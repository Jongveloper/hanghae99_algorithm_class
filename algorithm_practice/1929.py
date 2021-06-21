# isPrime 이라는 함수를 통해 소수를 구한다.

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


m, n = map(int, input().split())

# m 부터 n+1까지 i에 넣어주고 만약 i 가 소수라면 i를 출력한다.
for i in range(m, n+1):
    if isPrime(i):
        print(i)
