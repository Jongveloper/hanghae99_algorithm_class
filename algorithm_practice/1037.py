# 양수 A가 N의 진짜 약수가 되려면, N 이 A의 배수이고, A가 1 과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램
# N은 약수의 개수

N = int(input())
A = list(map(int, input().split()))

max_number = max(A)
min_number = min(A)

print(max_number * min_number)

# 약수가 모두 주어지기 때문에 가장 작은 값과 가장 큰 값을 곱하면 진짜 수를 구할 수 있다.
