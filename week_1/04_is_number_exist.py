input = [3, 5, 6, 1, 2, 4]


# 내 풀이
# def is_number_exist(number, array):
#
#     for i in array:
#         if i == number:
#             return True
#         else:
#             return False
#
#
# result = is_number_exist(3, input)
# print(result)
# 튜터님 풀이
def is_number_exist(number, array):
    for element in array:  # array 의 길이만큼 연산이 실행된다.
        if number == element:  # 비교 연산이 한번 실행된다.
            return True    # N * 1 = N 만큼

    return False


result = is_number_exist(3, input)
print(result)

# 내 풀이보다 튜터님의 풀이가 시간복잡도 면에서 더 좋은 것 같다.