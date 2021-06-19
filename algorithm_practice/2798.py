cards, number = map(int, input().split())
card = list(map(int, input().split()))
max_sum_card = 0


for i in range(cards):
    for j in range(i+1, cards):
        for k in range(j+1,  cards):
            sum_card = card[i] + card[j] + card[k]
            if sum_card > number:
                continue
            else:
                max_sum_card = max(max_sum_card, card[i] + card[j] + card[k])
print(max_sum_card)