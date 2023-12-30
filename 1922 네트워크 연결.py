import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
MAP = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    MAP[a][b] = c
    MAP[b][a] = c

dist = MAP[1].copy()
min_dist = min(dist)
idx = dist.index(min_dist)
visit = [False] * (n+1)
visit[1] = True
answer = 0

for i in range(1, n):
    if idx == -1:
        break
    answer += min_dist
    visit[idx] = True
    min_dist = INF
    min_idx = -1

    for j in range(1, n+1):
        if not visit[j] and dist[j] > MAP[idx][j]:
            dist[j] = MAP[idx][j]
        if not visit[j] and min_dist > dist[j]:
            min_dist = dist[j]
            min_idx = j

    idx = min_idx

print(answer)