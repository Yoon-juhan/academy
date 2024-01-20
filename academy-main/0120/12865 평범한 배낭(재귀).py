n, k = map(int, input().split())
info = [[0, 0]]
info += [list(map(int, input().split())) for _ in range(n)]

def dfs(x, sum):
    if x > n:
        return 0
    
    if dp[x][sum]:
        return dp[x][sum]

    a = 0
    if sum + info[x][0] <= k:
        a = dfs(x+1, sum+info[x][0]) + info[x][1]
    b = dfs(x+1, sum)

    dp[x][sum] = max(a, b)

    return dp[x][sum]

dp = [[0]*(k+1) for _ in range(n+1)]

print(dfs(1, 0))

