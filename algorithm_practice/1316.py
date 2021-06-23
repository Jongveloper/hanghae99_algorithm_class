n = int(input())

for _ in range(n):
    word = input()
    for i in range(len(word)-1):  # -1을 해주는 이유는 +1에 인덱스 범위초과 오류가 발생
        if word[i] != word[i+1]:  # word[i] 와 word[i+1]이 같지 않고 word[i]가 word[i+1:] 에 포함되어 있다면
            if word[i] in word[i+1:]:
                n -= 1  # n에서 1을 뺀다.
                break
print(n)