# words = input().upper()
# unique_words = list(set(words))
#
# cnt_list = []
#
# for char in unique_words:
#     cnt = words.count(char)  # words 에 있는 중복이 제거된 char 을 하나씩 넣어줍니다.
#     cnt_list.append(cnt)  # cnt_list 에 cnt 를 추가해줍니다.
# if cnt_list.count(max(cnt_list)) > 1:  # 만약 cnt_list 에 가장 큰 값 max(cnt) 를 count 함수를 이용해서 센 개수가 cnt_list 에 두개 이상이라면
#     print('?')  # ?를 출력하빈다.
# else:
#     max_index = cnt_list.index(max(cnt_list))  # 반복이 가능한 인자 중 가장 큰 데이터를 반환
#     print(unique_words[max_index])

words = input().upper()
unique_words = list(set(words))
