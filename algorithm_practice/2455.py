# 지능형 기차가 1번역(출발역)부터 4번역(종착역)까지 4개의 종착역이 있는 노선에서 운행됨
# 이 기차에는 타거나 내리는 사람수를 자동으로 인식할 수 있는 장치가 있음
# 이 장치를 이용하여 출발역엣거 종착역까지 가는 도중 기차 안에 사람이 가장 많을 때의 사람 수를 계산하려고 함
# 기차에 타는 사람들은 모두 내리고 탐

stations = 4
people = 0
most_station = []
for station in range(stations):
    get_off, take = map(int, input().split())
    people = people + take - get_off
    most_station.append(people)
print(max(most_station))