from collections import defaultdict

n = int(input())
tree = defaultdict(list)
nodes = list(map(int, input().split()))
remove_node = int(input())
answer = 0

for i in range(n):
    if i != remove_node:
        tree[nodes[i]].append(i)

if tree[remove_node]:
    del tree[remove_node]

def dfs(now):
    global answer

    for next in tree[now]:
        if not tree[next]:
            answer += 1
        dfs(next)

dfs(-1)

print(answer)