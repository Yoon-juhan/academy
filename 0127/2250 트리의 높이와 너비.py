from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
tree = {}
level = defaultdict(list)
child_node = set()

for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]
    child_node.add(b)
    child_node.add(c)

x = 1
def dfs(now, d):
    global x

    if now != -1:
        dfs(tree[now][0], d+1)
        level[d].append(x)
        x += 1
        dfs(tree[now][1], d+1)

root = 0
for i in range(1, n+1):
    if i not in child_node:
        root = i

dfs(root, 1)

answer = []

for key, value in level.items():
    width = max(value) - min(value) + 1
    answer.append([key, -width])

answer.sort(key=lambda x: (x[1], x[0]))

print(answer[0][0], -answer[0][1])