input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # 스페이스바는 포함하지 않기위해
            continue  # 스페이스바가 나오게되면 무시합니다.
        array_index = ord(char) - ord("a")  # 각 알파벳을 배열에 넣기위해 char - a(97(아스키 코드))를 합니다.
        alphabet_occurrence_array[array_index] += 1  # alphabet_occurrence_array[array_index] +1 합니다.

    max_occurrence = 0  # max_occurrence 를 담아줄 저장소
    max_alphabet_index = 0  # max_alphabet_index 를 담아줄 저장소
    for index in range(len(alphabet_occurrence_array)):  # 알파벳을 0~25 숫자로 변환하여 반복문을 통해 index 에 넣어줍니다.
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)