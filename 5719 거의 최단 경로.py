import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

start, end = map(int, input().split())

graph = defaultdict(list)
back_graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    back_graph[b].append((a, c))
    
INF = int(1e9)

def dijkstra(i):
    q = deque([(i, 0)])
    distance = [INF] * (n)
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

def dijkstra2(i):
    q = deque([(i, D[end])])
    distance = [INF] * (n)
    distance[i] = 0

    while q:
        now, now_dist = q.popleft()

        if distance[now] < now_dist:
            continue

        for next, next_dist in back_graph[now]:
            new_dist = now_dist - next_dist
            if D[next] != new_dist and distance[next] > new_dist:
                distance[next] = new_dist
                q.append((next, new_dist))

    return distance

D =  dijkstra(start)   # 최단경로
print('출력 :', dijkstra(start))

print(dijkstra2(end))