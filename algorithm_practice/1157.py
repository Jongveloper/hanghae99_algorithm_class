# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성 단, 대문자와 소문자 구분 x
# 입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어짐
# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력 단, 가장 많이 사용된 알파벳이 여러개 존재하는경우 ?를 출력

# 문제 접근 방식 : 대소문자 구분을 하지 않기 위해 모두 대문자로 변환
# 리스트로 받고 그 리스트에 같은 단어가 나오면 cnt += 1을 해준다?

words = list(input().upper())
most_word = list(set(words))

cnt_list = []

for i in most_word:
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
    print(cnt_list.count(max(cnt_list)))
else:
    max_index = cnt_list.index(max(cnt_list))
    print(most_word[max_index])