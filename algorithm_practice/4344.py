n = int(input())

for i in range(n):
    nums = list(map(int, input().split(' ')))  # 첫 줄에 시험 개수 / 둘째 줄 처음에 학생 수 / 이후 점수를 입력합니다.
    avg = sum(nums[1:]) / nums[0]  # 처음으로 들어가는 nums 는 학생 수 이므로 [0]을 제외하고 더해준 후 / [0](학생 수)를 해줍니다.
    cnt = 0  # 평균이 넘는 학생 수 저장소
    for score in nums[1:]:  # 점수를 넣어줍니다.
        if score > avg:  # 점수가 평균보다 크다면
            cnt += 1  # cnt 를 +1 해줍니다.
    rate = cnt / nums[0] * 100  # 평균이 넘는 학생을 학생수로 나누어 100을 곱해줍니다.
    print(f"{rate:.3f}%")

