import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

INF = int(1e9)
distance = [INF] * (n+1)
distance[start] = 0
via = [-1] * (n+1)
q = deque([(start, 0)])

while q:
    now, dist = q.popleft()

    if distance[now] < dist:
        continue

    for next, next_dist in graph[now]:
        new_dist = dist + next_dist
        if distance[next] > new_dist:
            distance[next] = new_dist
            via[next] = now
            q.append((next, new_dist))

i = end
via2 = []
print(distance[end])
while i != start:
    via2.append(via[i])
    i = via[i]

print(len(via2)+1)
print(*via2[::-1], end)