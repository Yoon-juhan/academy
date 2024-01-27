from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
tree = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = [0] * (n+1)
visit = [0] * (n+1)
visit[1] = 1

def dfs(now):
    
    for next in tree[now]:
        if visit[next] == 0:
            answer[next] = now  # 부모 저장
            visit[next] = 1
            dfs(next)

dfs(1)

for i in range(2, n+1):
    print(answer[i])