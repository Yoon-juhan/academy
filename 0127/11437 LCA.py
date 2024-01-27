from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

level = [0] * (n+1)
visit = [0] * (n+1)
visit[1] = 1

def dfs(now, parent, l):
    level[now] = [parent, l]

    for next in tree[now]:
        if not visit[next]:
            visit[next] = 1
            dfs(next, now, l+1)

dfs(1, -1, 1)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    while True:
        if a == b:
            print(a)
            break
        # 부모 같으면
        if level[a][0] == level[b][0]:
            print(level[a][0])
            break
        elif level[a][1] == level[b][1] and level[a][0] != level[b][0]:
            a = level[a][0]
            b = level[b][0]
        elif level[a][1] > level[b][1]:
            a = level[a][0]
        else:
            b = level[b][0]