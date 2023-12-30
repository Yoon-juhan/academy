import sys
from collections import deque
input = sys.stdin.readline
# 소문자 - 96
# 대문자 - 38
n = int(input())

INF = int(1e9)
MAP = [[INF] * (n+1) for _ in range(n+1)]
answer = 0

for i in range(1, n+1):
    data = input()
    for j in range(1, n+1):

        if data[j-1] != '0':
            x = ord(data[j-1])
            if x > 90: # 소문자
                answer += x - 96
                if i != j and MAP[i][j] > x - 96:
                    MAP[i][j] = x - 96
                    MAP[j][i] = x - 96
            else: # 대문자
                answer += x - 38
                if i != j:
                    MAP[i][j] = x - 38
                    MAP[j][i] = x - 38

for i in MAP:
    print(i)

dist = MAP[1]
q = deque([[1, 0]])
chk = [False] * (n+1)
chk[1] = True

while q:
    node, d = q.popleft()
    
    min_dist = INF
    for i in range(1, n+1):
        if not chk[i] and min_dist > dist[i]:
            min_dist = dist[i]
            next_node = i

    if min_dist != INF:
        q.append([next_node, min_dist+d])
        chk[next_node] = True

        for i in range(1, n+1):
            if not chk[i] and dist[i] > MAP[next_node][i]:
                dist[i] = MAP[next_node][i]

for i in range(1, len(chk)):
    if not chk[i]:
        print(-1)
        exit()

print(answer - d)