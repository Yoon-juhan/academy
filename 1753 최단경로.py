import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 가중치, 다음 노드

INF = int(1e9)
distance = [INF] * (V+1)
distance[start] = 0
q = [(0, start)]

while q:
    now_dist, now = heappop(q)

    if distance[now] < now_dist:
        continue

    for next_dist, next in graph[now]:
        new_dist = now_dist + next_dist
        if distance[next] > new_dist:
            distance[next] = new_dist
            heappush(q, (new_dist, next))

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])