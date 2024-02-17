import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

lines = []
for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        b += n
    lines.append((a, b, i+1))
    if b < n:
        lines.append((a+n, b+n, i+1))

lines.sort(key=lambda x : (x[0], -x[1]))

end = lines[0][1]

remove = set()
for i in range(len(lines)-1):
    if end >= lines[i+1][1]:
        remove.add(lines[i+1][2])
    else:
        end = lines[i+1][1]

for i in range(1, m+1):
    if i not in remove:
        print(i, end=" ")