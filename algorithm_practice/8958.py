n = int(input())
for i in range(n):
    a = input()
    a_list = list(a)
    cnt = 1
    total = 0
    for j in a_list:
        if j == "O":
            total += cnt
            cnt += 1
        else:
            cnt = 1
    print(total)