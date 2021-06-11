input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # 스페이스바는 포함하지 않기위해
            continue  # 스페이스바가 나오게되면 무시합니다.
        array_index = ord(char) - ord("a")  # 각 알파벳을 배열에 넣기위해 char - a(97(아스키 코드))를 합니다.
        alphabet_occurrence_array[array_index] += 1  # alphabet_occurrence_array[array_index] +1 합니다.

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char



result = find_not_repeating_character(input)
print(result)