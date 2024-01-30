from collections import defaultdict
import sys
input = sys.stdin.readline

V = int(input())
tree = defaultdict(list)

for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info)-1, 2):
        tree[info[0]].append([info[i], info[i+1]])

visit = [False] * (V+1)
visit[1] = True
distance = 0

def dfs(now, d):
    global distance
    left, right = 0, 0

    for next, next_d in tree[now]:
        x = 0
        if not visit[next]:
            visit[next] = True
            x = dfs(next, next_d)
        if left <= right:
            left = max(left, x)
        else:
            right = max(right, x)
    
    distance = max(distance, left + right)
    return max(left+d, right+d)

dfs(1, 0)

print(distance)