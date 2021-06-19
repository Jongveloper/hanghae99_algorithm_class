n = int(input())
result = 0
for i in range(n+1):
    str_n = map(int, str(i))
    result = n + sum(str_n)
    if result == n:
        print(result)
    if str_n != n:
        print(0)