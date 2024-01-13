import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
answer = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(now_node):
    q = deque([now_node])

    while q:
        now_node = q.popleft()

        for next_node in graph[now_node]:
            if not visit[next_node]:
                visit[next_node] = True
                answer[now] += 1
                q.append(next_node)

for now in range(1, n+1):
    visit = [False] * (n+1)
    visit[now] = True
    bfs(now)

max_value = max(answer)

for i in range(1, n+1):
    if answer[i] == max_value:
        print(i, end=" ")