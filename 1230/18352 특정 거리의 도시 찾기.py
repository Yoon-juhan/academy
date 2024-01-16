from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = int(1e9)
dist = [INF] * (n+1)
dist[x] = 0

q = [(0, x)]

while q:
    d, now = heappop(q)

    if d > dist[now]:
        continue

    for next in graph[now]:
        if dist[next] > d + 1:
            dist[next] = d + 1
            heappush(q, (d + 1, next))

sw = True
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        sw = False

if sw:
    print(-1)