import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(x, y):

    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and MAP[x][y] > MAP[nx][ny]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

m, n = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

print(dfs(0,0))