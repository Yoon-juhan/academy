n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

for i in MAP:
    print(i)

def dfs(x, y):
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == n and y == m:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx, ny = x + mx[i], y + my[i]

        if 0 <= nx < n and 0 <= ny < m and MAP[x][y] > MAP[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]
            

dp = [[-1] * m for _ in range(n)]

mx, my = [0, 0, 1, -1], [1, -1, 0, 0]

dfs(0, 0)

for i in dp:
    print(i)