from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if not heap and x == 0:
        print(0)
    elif x > 0:
        heappush(heap, x)
    else:
        print(heappop(heap))