cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]  # 크로아티아 알파벳 리스트입니다.
word = input()

for i in cro:  # cro 리스트의 원소를 i에 넣어줍니다.
    word = word.replace(i, '*')  # i 즉, input 을 받은 word 에 i 가 포함되어있다면 *로 바꿔줍니다.
print(len(word))  # 문자열로 바꿔준다면 cro 에 두글자~세글자를 한 글자로 인식합니다!