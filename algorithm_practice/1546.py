# 기말고사를 망친 세준이 성적표 조작을 한다.
# ex) 세준이 최고점 70 , 수학점수 50 이라하면 점수계산법 : 50(수학점수) / 70(최고점)*100 = 71.43
# 이 방법으로 했을 때의 평균 구하기

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_score = []

for i in scores:
    i = i / max_score * 100
    new_score.append(i)
    avg = sum(new_score) / n
print(avg)
