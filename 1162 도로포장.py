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

INF = int(1e9)


distance = [[INF] * (n+1) for _ in range(n+1)]
distance[1][1] = 0

q = [(0, 1, 1)]

while q:
    now_d, now, cnt = heappop(q)

    if distance[cnt][now] < now_d: 
        continue

    for next_d, next in graph[now]:
        new_d = now_d + next_d
        if distance[cnt][next] > new_d:
            distance[cnt][next] = new_d
            heappush(q, (new_d, next, cnt))
        if cnt+1 <= k+1 and distance[cnt+1][next] > now_d:
            distance[cnt+1][next] = now_d
            heappush(q, (now_d, next, cnt+1))

for i in distance:
    print(i)