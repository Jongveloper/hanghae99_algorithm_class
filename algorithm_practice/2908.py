a, b = list(map(str, input().split()))

a_list = list(a)
a_list.reverse()
b_list = list(b)
b_list.reverse()
a_total = a_list[0] + a_list[1] + a_list[2]
b_total = b_list[0] + b_list[1] + b_list[2]
int(a_total)
int(b_total)
print(max(a_total, b_total))