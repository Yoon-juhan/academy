from collections import defaultdict

n = int(input())
m = int(input())
    
def union(a, b):
    x = find(a)
    y = find(b)
    parent[y] = x

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

parent = [i for i in range(n+1)]
E = defaultdict(list)   # 원수 그래프

for i in range(m):
    relation = input().split()
    a, b = int(relation[1]), int(relation[2])

    if relation[0] == 'F':
        union(a, b)
    else:
        E[a].append(b)
        E[b].append(a)

for k in E:             # 나
    for i in E[k]:      # 내 원수
        for j in E[i]:  # 내 원수의 원수
            union(k, j) # (나, 나의 원수의 원수) union

answer = set()
for i in range(1, n+1):
    answer.add(find(parent[i]))

print(len(answer))