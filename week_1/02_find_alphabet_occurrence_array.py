def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # 스페이스바는 포함하지 않기위해
            continue  # 스페이스바가 나오게되면 무시합니다.
        array_index = ord(char) - ord("a")  # 각 알파벳을 배열에 넣기위해 char - a(97(아스키 코드))를 합니다.
        alphabet_occurrence_array[array_index] += 1  # alphabet_occurrence_array[array_index] +1 합니다.

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
