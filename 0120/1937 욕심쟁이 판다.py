n = int(input())

MAP = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
mx, my = [0, 0, 1, -1], [1, -1, 0, 0]
sort_MAP = []
for i in range(n):
    for j in range(n):
        sort_MAP.append([MAP[i][j], i, j])

sort_MAP.sort()
answer = -1

for v, x, y in sort_MAP:
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + mx[i], y + my[i]
        if 0 <= nx < n and 0 <= ny < n:
            if v > MAP[nx][ny]:
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    answer = max(answer, dp[x][y])

print(answer)