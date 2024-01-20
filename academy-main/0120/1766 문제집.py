from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []

for i in range(1, n+1):
    if not indegree[i]:
        heappush(q, i)

while q:
    now = heappop(q)
    print(now, end=" ")

    for next in graph[now]:
        indegree[next] -= 1
        if not indegree[next]:
            heappush(q, next)