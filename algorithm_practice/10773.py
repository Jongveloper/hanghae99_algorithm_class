# 재민이는 돈을 실수로 잘못 부르는 사고를 침
# 재현이는 재민이가 잘못된 수를 부를 때 0 을 외쳐 재민이가 가장 최근에 재민이가 쓴 수를 지우게함 (pop)
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고싶어함 sum([])

n = int(input())  # 재민이가 부를 수
n_list = []  # 재민이가 부른 수의 저장소

for i in range(n):
    true_n = int(input())  # 재민이가 부른 수
    if true_n == 0:
        n_list.pop()  # 0을 외치면 가장 최근에 재민이가 쓴 수를 지움
    else:
        n_list.append(true_n)  # 0을 외치지 않았다면 저장소에 추가해줌
print(sum(n_list))
