import sys
input = sys.stdin.readline

V, E = map(int, input().split())

parent = [0]
for i in range(1, V+1):
    parent.append(i)

e = [tuple(map(int, input().split())) for _ in range(E)]
e.sort(key=lambda x : x[2])

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

answer = 0
for a, b, c in e:
    if find(a) != find(b):
        answer += c
        union(a, b)

print(answer)