from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)