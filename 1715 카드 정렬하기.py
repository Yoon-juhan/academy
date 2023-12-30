from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):  # 카드 묶음 생성
    heappush(heap, int(input()))

answer = 0
while len(heap) >= 2:
    x = heappop(heap) + heappop(heap)
    heappush(heap, x)
    answer += x

print(answer)