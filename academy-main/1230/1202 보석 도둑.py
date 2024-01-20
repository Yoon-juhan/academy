from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

jewelry = []

for _ in range(n):
    m, v = map(int, input().split())
    jewelry.append((m, v))

bag = [int(input()) for _ in range(k)]

jewelry.sort()  # 무게 오름차순 정렬
bag.sort()      # 가방 크기 오름차순 정렬

idx, answer = 0, 0
price = []      # 보석 가격 담을 힙

for b in bag:

    while idx < len(jewelry) and b >= jewelry[idx][0]:  # i번 가방에 담을 수 있는 보석 다 담기
        heappush(price, -jewelry[idx][1])
        idx += 1

    if price:   # 담은 보석이 있으면 가장 비싼 보석을 선택
        answer += -heappop(price)

print(answer)