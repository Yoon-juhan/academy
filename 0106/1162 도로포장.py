import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

INF = int(1e12)

distance = [[INF] * (k+1) for _ in range(n+1)]
distance[1][0] = 0

q = [(0, 1, 0)]

while q:
    now_d, now, cnt = heappop(q)

    if distance[now][cnt] < now_d: 
        continue

    for next_d, next in graph[now]:
        new_d = now_d + next_d
        if distance[next][cnt] > new_d:
            distance[next][cnt] = new_d
            heappush(q, (new_d, next, cnt))
        if cnt+1 <= k and distance[next][cnt+1] > now_d:
            distance[next][cnt+1] = now_d
            heappush(q, (now_d, next, cnt+1))

print(min(distance[-1]))