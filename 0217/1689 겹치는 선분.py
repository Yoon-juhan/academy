import sys

lines = []
n = int(input())
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    lines.append((s, 1))
    lines.append((e, -1))

lines.sort()
result = 0
cnt = 0

for line in lines:
    cnt += line[1]
    result = max(result, cnt)

print(result)