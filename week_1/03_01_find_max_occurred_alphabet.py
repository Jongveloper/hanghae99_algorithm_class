input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                      "j", "k", "l", "m", "n", "o", "p", "q", "r",
                      "s", "t", "u", "v", "w", "x", "y", "z"]  # 알파벳 배열을 만들어 줍니다.
    max_occurrence = 0  # 큰 값을 저장할 변수입니다.
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:  # 반복문을 돌며 문자열의 문자와 동일하다면
                occurrence += 1  # occurrence + 1 해줍니다.

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet 

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)