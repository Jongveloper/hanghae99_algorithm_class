input = 20


def find_prime_list_under_number(number):
    prime_list = []  # 빈 리스트를 만들어 준다.(소수 담을 용도)
    for n in range(2, number + 1):  # 2~20까지 n에 넣어주는 반복문!
        for i in prime_list:
            if n % i == 0 and i * i <= n:  # n 나누기 i 를 했을 때 0이거나 i의 제곱근이 n보다 크거나 같을 때 소수이기 때문에
                break  # 반복문을 멈춰주고
        else:
            prime_list.append(n)  # 빈 리스트에(소수)를 담습니다.
    return prime_list


result = find_prime_list_under_number(input)
print(result)


# 어떻게 프로그램이 작동하는지
# n     i       prime_list              if문
# 2    null        []         빈 리스트이기 때문에 for 문이 실행이 되지않아 2를 리스트에 담습니다!
# 3     [2]        [2]        3 % 2 != 0 // 4 <= 3 -> 4가 3보다 크기 때문에 리스트(3)담습니다!
# 4    [2,3]      [2,3]       4 % 2 == 0 // 4 <= 4 -> if 조건 성립!!
# 5    [2,3]      [2,3]       5 % 2 != 0 // 5 % 3 != 0 -> 5를 리스트(5)담습니다!
# .... 이런식으로 동작합니다....!
