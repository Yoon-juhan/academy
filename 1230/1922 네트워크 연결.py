import sys
from heapq import heappop, heappush
from collections import defaultdict

n = int(input())
m = int(input())

tree = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    tree[a].append((c, b))  # 비용 먼저
    tree[b].append((c, a))  # 양방향

heap = [(0, 1)]             # 비용, 노드
visit = [False] * (n+1)
answer = 0

while heap:
    cost, node = heappop(heap)

    if not visit[node]:
        visit[node] = True
        answer += cost

        for next_cost, next_node in tree[node]:
            heappush(heap, (next_cost, next_node))

print(answer)