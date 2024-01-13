from collections import defaultdict, deque
import sys
input = sys.stdin.readline

K = int(input())

def bfs(n):
    q = deque([n])
    visit[n] = 1

    while q:
        now = q.popleft()

        for next in graph[now]:
            if not visit[next]:
                if visit[now] == 1:
                    visit[next] = 2
                    q.append(next)
                else:
                    visit[next] = 1
                    q.append(next)
            elif visit[now] == visit[next]:
                return 0

    return 1

for _ in range(K):
    V, E = map(int, input().split())

    graph = defaultdict(list)
    visit = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if not visit[i]:
            answer = bfs(i)
            
            if not answer:
                print("NO")
                break
    else:
        print("YES")