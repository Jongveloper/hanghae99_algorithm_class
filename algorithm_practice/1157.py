# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성 단, 대문자와 소문자 구분 x
# 입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어짐
# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력 단, 가장 많이 사용된 알파벳이 여러개 존재하는경우 ?를 출력

# 문제 접근 방식 : 대소문자 구분을 하지 않기 위해 모두 대문자로 변환

words = input().upper()
set_words = list(set(words))
max_word_cnt = []

for word in set_words:
    word = words.count(word)
    max_word_cnt.append(word)

if max_word_cnt.count(max(max_word_cnt)) > 1:
    print("?")
else:
    max_index = max_word_cnt.index(max(max_word_cnt))
    print(set_words[max_index])