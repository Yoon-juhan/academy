from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
ant = [int(input()) for _ in range(n)]

tree = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))

def dfs(now, parent, distance):
    info[now] = [parent, distance]   # 부모, 가중치

    for next, d in tree[now]:
        dfs(next, now, d)

arr = []
info = [[0, 0] for _ in range(n+1)] 

dfs(1, 0, 0)
arr.append(info)

x = 1
while 2 ** x <= n:
    info = [[0, 0] for _ in range(n+1)] 
    before = arr[x-1]

    for i in range(n, -1, -1):
        info[i][0] = before[before[i][0]][0]
        info[i][1] = before[i][1] + before[before[i][0]][1]

    arr.append(info)
    x += 1

for i in range(n):
    e = ant[i]
    u = i+1

    for j in range(len(arr)-1, -1, -1):
        if e >= arr[j][u][1]:
            e -= arr[j][u][1]
            u = arr[j][u][0]
            if e <= 0:
                break
    
    if u == 0: u = 1
    print(u)