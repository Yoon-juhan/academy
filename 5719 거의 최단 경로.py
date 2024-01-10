import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dijkstra(start):
    q = deque([(start, 0)])
    distance = [INF] * (n)
    distance[start] = 0


    while q:
        now, now_dist = q.popleft()

        if distance[now] < now_dist:
            continue

        for i in range(n):
            new_dist = now_dist + graph[now][i]
            if distance[i] > new_dist:
                distance[i] = new_dist
                q.append((i, new_dist))

    return distance

def remove(end):
    q = deque([end])
    
    while q:
        now = q.popleft()

        for i in range(n):
            if D[i] + graph[i][now] == D[now]:
                q.append(i)
                graph[i][now] = INF

while True:
    n, m = map(int, input().split())
    if n + m == 0: break
    
    start, end = map(int, input().split())

    INF = int(1e9)
    graph = [[INF] * n for _ in range(n)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    
    D = dijkstra(start)   # 최단경로
    remove(end)
    
    answer = dijkstra(start)
    if answer[end] != INF:
        print(answer[end])
    else:
        print(-1)