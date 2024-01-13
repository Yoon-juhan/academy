from collections import defaultdict

n = int(input())
cards = map(int, input().split())
m = int(input())
my_cards = map(int, input().split())

hash = [[] for _ in range(500009)]

# 해시 태이블 생성
for card in cards:
    tmp = hash[card % 500009]
    for t in tmp:
        if t[0] == card:
            t[1] += 1
            break
    else:
        hash[card % 500009].append([card, 1])

answer = []
for my_card in my_cards:
    tmp = hash[my_card % 500009]

    for t in tmp:
        if t[0] == my_card:
            answer.append(t[1])
            break
    else:
        answer.append(0)

print(*answer)