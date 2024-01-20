n, k = map(int, input().split())

info = [[0, 0]]
for _ in range(n):
    w, v = map(int, input().split())
    info.append((w, v))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = info[i]
    for j in range(1, k+1):
        if j >= w:  # 가방 크기가 보석보다 크면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            print(dp[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])