n = int(input())

result = 0
for i in range(n + 1):
    str_i = map(int, str(i))
    result = i + sum(str_i)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)