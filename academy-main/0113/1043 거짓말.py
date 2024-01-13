import sys
input = sys.stdin.readline

n, m = map(int, input().split())

true = list(map(int, input().split()))  # 진실을 아는 사람 수, 번호

parent = [i for i in range(n+1)]

def union(a, b):
    x = find(a)
    y = find(b)
    parent[max(x, y)] = min(x, y)

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    people = list(map(int, input().split()))  # 파티에 오는 사람 수, 번호
