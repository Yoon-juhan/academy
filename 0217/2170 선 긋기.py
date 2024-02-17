import sys
input = sys.stdin.readline
n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

start, end = lines[0][0], lines[0][1]

answer = 0

for i in range(1, len(lines)):
    if end >= lines[i][1]:  # 겹치는 선
        continue
    if lines[i][0] <= end < lines[i][1]:
        end = lines[i][1]
    else:
        answer += end - start
        start, end = lines[i][0], lines[i][1]
        
print(answer + end - start)