from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))

def dfs(now):
    global answer
    max_a, max_b = 0, 0

    for next, d in tree[now]:
        t = dfs(next) + d
        if max_a < t:
            max_b, max_a = max_a, t
        elif max_b < t:
            max_b = t

    answer = max(answer, max_a + max_b)
    
    return max_a

answer = -1
dfs(1)

print(answer)