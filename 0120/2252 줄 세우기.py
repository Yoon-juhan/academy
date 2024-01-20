from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

q = deque([])
answer = []
for i in range(1, n+1): # 진입간선 0이면 큐에 추가
    if not indegree[i]:
        q.append(i)

while q:
    now = q.popleft()
    answer.append(now)

    for next in graph[now]:
        indegree[next] -= 1     # 간선 지우기
        if not indegree[next]:
            q.append(next)

print(*answer)