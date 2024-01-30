from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))

answer = 0

def dfs(now, d):
    global answer
    left, right = 0, 0

    for next, next_d in tree[now]:
        x = dfs(next, next_d)
        if left <= right:
            left = max(left, x)
        else:
            right = max(right, x)
    
    answer = max(answer, left + right)
    return max(left+d, right+d)

dfs(1, 0)

print(answer)