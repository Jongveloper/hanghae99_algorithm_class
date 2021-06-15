words = input().upper()  # 대문자로 출력해야하기 때문에 대문자로 바꿔준다.
unique_words = list(set(words))  # 중복을 제거한다.

cnt_list = []

for char in unique_words:
    cnt = words.count(char)  # words 에 unique_words 를 넣어주고 words 에 포함되어 있는 알파벳을 세어줍니다.
    cnt_list.append(cnt)  # cnt_list 에  word.count(char) 를 추가해줍니다.
if cnt_list.count(max(cnt_list)) > 1:  # 만약 cnt_list 에 가장 큰 값 max(cnt) 를 count 함수를 이용해서 센 개수가 cnt_list 에 두개 이상이라면
    print('?')  # ?를 출력합니다.
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
    print(max_index)
