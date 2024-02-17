n = int(input())

coordinate = []
for _ in range(n):
    coordinate.append(list(map(int, input().split())))

parent = [i for i in range(n+1)]

def union(a, b):
    x = find(a)
    y = find(b)
    parent[y] = x

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def ccw(x1, x2, x3, y1, y2, y3):
    return (x1* y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

for i in range(len(coordinate)-1):
    x1, y1, x2, y2, x3, y3, x4, y4 = coordinate[i][0], coordinate[i][1], coordinate[i][2], coordinate[i][3], coordinate[i+1][0], coordinate[i+1][1], coordinate[i+1][2], coordinate[i+1][3]

    a = ccw(x1, x2, x3, y1, y2, y3)
    b = ccw(x1, x2, x4, y1, y2, y4)
    c = ccw(x3, x4, x1, y3, y4, y1)
    d = ccw(x3, x4, x2, y3, y4, y2)

    n, m = a * b, c * d

    if n == 0 and m == 0:
        if (min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4)):
            union(i+1, i+2)
    elif n <= 0 and m <= 0:
        union(i+1, i+2)

print(parent)
group = set()
for i in range(2, len(parent)):
    group.add(find(parent[i]))

print(len(group))

answer = -1
for i in list(group):
    answer = max(parent.count(i), answer)

print(answer)