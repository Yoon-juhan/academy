import sys
input = sys.stdin.readline

n, m = map(int, input().split())

info = [list(map(int, input().split())) for i in range(m)]
INF = int(1e12)
distance = [INF] * (n+1)
distance[1] = 0

for i in range(1, n+1):
    flag = False
    for j in range(len(info)):
        now, next, dist = info[j]

        if distance[now] == INF:
            continue

        new_dist = distance[now] + dist

        if distance[next] > new_dist:
            distance[next] = new_dist
            flag = True

if flag:
    print(-1)
else:
    for i in range(2, len(distance)):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])