from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)
indegree = [0] * (n+1)
time = [0] * (n+1)
answer = [0] * (n+1)

for i in range(1, n+1):
    lst = list(map(int, input().split()))
    j = 0
    while lst[j] != -1:
        if j == 0:
            time[i] = lst[j]
        else:
            graph[lst[j]].append(i)
            indegree[i] += 1
        j += 1

q = deque([])
for i in range(1, n+1):
    if not indegree[i]:
        answer[i] = time[i]
        q.append(i)

while q:
    now = q.popleft()

    for next in graph[now]:
        indegree[next] -= 1
        answer[next] = max(answer[next], answer[now] + time[next])
        if not indegree[next]:
            q.append(next)

for i in range(1, len(answer)):
    print(answer[i])