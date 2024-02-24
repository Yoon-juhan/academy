import sys
input = sys.stdin.readline

n, m, t, d = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
time = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(m):
        if "A" <= graph[i][j] <= "Z":
            graph[i][j] = ord(graph[i][j])-65
        else:
            graph[i][j] = ord(graph[i][j])-71

for i in graph:
    print(i)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] >  graph[i][k] + graph[k][j]:
                time[i][j] += 1
            else:
                if graph[i][k] + graph[k][j] - graph[i][j] < t:
                    time[i][j] += (graph[i][k] + graph[k][j] - graph[i][j]) ** 2

for i in time:
    print(i)