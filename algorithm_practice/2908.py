# 입력 값 a,b 를 받는데 a, b를 역순으로 하여 더 큰 수를 출력 ex) 734 => 437
a, b = list(map(str, input().split()))
a_list = list(a)
a_list.reverse()  # 리스트를 역순으로
b_list = list(b)
b_list.reverse()
a_total = a_list[0] + a_list[1] + a_list[2]  # 역순으로 한 값을 합쳐준다 (현재 스트링 형태이기 때문에 문자 더하기가 된다.)
b_total = b_list[0] + b_list[1] + b_list[2]
int(a_total)  # 데이터타입을 int 로 바꿔준다.
int(b_total)
print(max(a_total, b_total))  # 둘 중 큰 값을 출력해준다.
