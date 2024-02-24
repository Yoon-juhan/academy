import sys
input = sys.stdin.readline

n, m = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(m)]

INF = int(1e12)
distance = [-INF] * (n+1)
distance[1] = 0
path = [0] * (n+1)

for i in range(1, n+1):
    for j in range(len(info)):
        now, next, dist = info[j]

        if distance[now] == -INF:
            continue

        new_dist = distance[now] + dist
        if distance[next] < new_dist:
            distance[next] = new_dist
            path[next] = now
            if i == n:
                distance[next] = INF
                
answer = []
now = n

if distance[n] == INF:  # 도착점에 간섭을 주는 사이클이면
    print(-1)
else:
    while now != 1:
        answer.append(now)
        now = path[now]
    answer.append(1)
    print(*reversed(answer))