import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)
total = 0   # 들고있는 전체 랜선의 길이

for i in range(n):
    string = input()
    for j in range(n):
        if ord("a") <= ord(string[j]) <= ord("z"):      # 소문자
            dist = ord(string[j]) - ord("a") + 1
            tree[i].append((dist, j))                   # 길이 먼저
            tree[j].append((dist, i))

        elif ord("A") <= ord(string[j]) <= ord("Z"):    # 대문자
            dist = ord(string[j]) - ord("A") + 27
            tree[i].append((dist, j))
            tree[j].append((dist, i))
        else:                                           # '0'
            dist = 0
        if dist != 0:
            total += dist

heap = [(0, 0)]
visit = [False] * (53)  # Z = 52

while heap:
    d, node = heappop(heap)

    if not visit[node]:     # 방문 안했으면
        visit[node] = True  # 방문 처리
        total -= d          # 사용한 랜선 빼주기

        for next_d, next_node in tree[node]:    # 현재 노드랑 연결된 선 정보 추가
            heappush(heap, (next_d, next_node))

for i in range(n):
    if not visit[i]:
        print(-1)
        exit(0)

print(total)