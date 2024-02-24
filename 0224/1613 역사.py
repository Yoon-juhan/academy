import sys
input = sys.stdin.readline

n, k = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = -1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
                continue
            if graph[i][k] == 1 and  graph[k][j] == 1:
                graph[i][j] = 1
            elif graph[i][k] == -1 and  graph[k][j] == -1:
                    graph[i][j] = -1

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b])
