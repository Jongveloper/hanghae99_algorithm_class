import math

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    check = [True] * (2 * n + 1)
    for i in range(2, int(math.sqrt(2 * n) + 1)):
        if check[i]:
            j = 2
            while i * j <= 2 * n:
                check[i * j] = False
                j += 1
    for x in range(n+1, 2 * n + 1):
        if check[x]:
            count += 1
    print(count)