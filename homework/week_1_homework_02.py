input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0  # 모두 0으로 바꾸는 횟수 저장소
    count_to_all_one = 0  # 모두 1로 바꾸는 횟수 저장소


    if string[0] == 0:  # 만약 0으로 시작하면
        count_to_all_one += 1  # 0으로 바꾸는 횟수 저장소를 +1 해줍니다.
    elif string[0] == 1:  # 0으로 시작하지 않고 1로 시작한다면
        count_to_all_zero += 1  # 1으로 바꾸는 횟수 저장소를 +1 해줍니다.

    for i in range(len(string) - 1):  # 0부터 string 의 길이-1 만큼 i에 넣어줍니다.
        if string[i] != string[i + 1]:  # 만약 string[i]가 string[i + 1]과 같지 않고
            if string[i + 1] == '0':  # string[i + 1]문자열이 0이라면
                count_to_all_one += 1  # 모두 1로 바꾸는 횟수 저장소를 +1 해줍니다.
            if string[i + 1] == '1':  # 만약 string[i + 1]문자열이 1이라면
                count_to_all_zero += 1  # 모두 0으로 바꾸는 횟수 저장소를 +1 해줍니다.
    return min(count_to_all_one, count_to_all_zero)  # 0으로 바꾸는 횟수저장소와 1로바꾸는 횟수저장소 중 최솟값을 return 해줍니다.


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 동작 방식
# i     string[i]    != / ==    string[i + 1]     0count    1count
# 0       "0"          !=           "1"            +1         0
# 1       "1"          ==           "1"             1         0
# 2       "1"          ==           "1"             1         0
# 3       "1"          ==           "1"             1         0
# 4       "1"          !=           "0"             1        +1

