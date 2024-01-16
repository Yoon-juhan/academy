import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def union(a, b):
    x = find(a)
    y = find(b)
    
    if x != y:
        parent[y] = x

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")