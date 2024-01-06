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

def dijkstra(i):
    distance = [INF] * (n+1)
    distance[i] = 0

    q = [(0, i)]

    while q:
        now_d, now = heappop(q)

        if distance[now] < now_d: 
            continue

        for next_d, next in graph[now]:
            new_d = now_d + next_d
            if distance[next] > new_d:
                distance[next] = new_d
                heappush(q, (new_d, next))

    return distance