import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0]
for i in range(1, n+1):
    parent.append(i)

def union(a, b):
    x = find(a)
    y = find(b)
    parent[max(x, y)] = min(x, y)

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

for i in range(1, n+1):
    e = list(map(int, input().split()))
    for j in range(1, n+1):
        if e[j-1] == 1:
            union(i, j)

plan = list(map(int, input().split()))
start = parent[plan[0]]

for i in range(1, m):
    if  start != parent[plan[i]]:
        print("NO")
        break
else:
    print("YES")