from collections import defaultdict
import sys
input = sys.stdin.readline

V = int(input())
tree = defaultdict(list)
INF = int(1e9)

for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info)-1, 2):
        tree[info[0]].append([info[i], info[i+1]])

print(tree)

def dfs(now, d):
    if distance[1] < d:
        distance[0] = now
        distance[1] = d

    if visit[now]:
        return
    for next, next_d in tree[now]:
        visit[next] = True
        dfs(next, d+next_d)

visit = [False] * (V+1)
distance = [-1, -1]
dfs(1, 0)

print(distance)