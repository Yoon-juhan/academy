import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, x = map(int, input().split()) # 마을 수, 도로 수, 도착지

graph = defaultdict(list)
graph2 = defaultdict(list)
INF = int(1e9)

for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d)) # 도착지, 거리
    graph2[e].append((s, d)) # 도착지, 거리

def dijkstra(i, g):
    distance = [INF] * (n+1)
    distance[i] = 0
    q = deque([(i, 0)])

    while q:
        now, now_dist = q.popleft()

        if distance[now] < now_dist:
            continue

        for next, next_dist in g[now]:
            new_dist = now_dist + next_dist
            if distance[next] > new_dist:
                distance[next] = new_dist
                q.append((next, new_dist))

    return distance

go = dijkstra(x, graph)
back = dijkstra(x, graph2)

answer = -1
for i in range(1, n+1):
    if answer < go[i] + back[i]:
        answer = go[i] + back[i]

print(answer)