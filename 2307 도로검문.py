import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

start, end = 1, n
INF = int(1e9)

def dijkstra(i, x):
    distance = [INF] * (n+1)
    distance[i] = 0

    q = [(0, i)]

    while q:
        now_d, now = heappop(q)

        if distance[now] < now_d: 
            continue

        for next_d, next in graph[now]:
            new_d = now_d + next_d
            if next != x and distance[next] > new_d:
                distance[next] = new_d
                heappush(q, (new_d, next))

    return distance

D = dijkstra(start, -1) # 경찰이 안 막았을 때

answer = -1
for x in range(1, n):
    d = dijkstra(start, x)
    if d[n] == INF:
        print(-1)
        exit()
    answer = max(answer, d[n] - D[n])

print(answer)