import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, e = map(int, input().split())

graph = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())   # 꼭 가야되는 길

INF = int(1e9)

def dijkstra(i):
    q = deque([(i, 0)])
    distance = [INF] * (n+1)
    distance[i] = 0

    while q:
        now, now_dist = q.popleft()

        if distance[now] < now_dist:
            continue

        for next, next_dist in graph[now]:
            new_dist = now_dist + next_dist
            if distance[next] > new_dist:
                distance[next] = new_dist
                q.append((next, new_dist))

    return distance

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

answer1 = d1[v1] + d2[v2] + d3[n]
answer2 = d1[v2] + d3[v1] + d2[n]

answer = min(answer1, answer2)

if answer >= INF:
    print(-1)
else:
    print(answer)