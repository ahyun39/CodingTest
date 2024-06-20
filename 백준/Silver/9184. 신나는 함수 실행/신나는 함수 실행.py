def w_dp(a, b, c):
    MAX = 21
    dp = [[[0 for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]

    for i in range(MAX):
        for j in range(MAX):
            for k in range(MAX):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 1
    for i in range(1, MAX):
        for j in range(1, MAX):
            for k in range(1, MAX):
                if i < j and j < k:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return dp[20][20][20]
        return dp[a][b][c]
    
    return w(a, b, c)

while True:
    a, b, c = map(int,input().split())
    if a == b == c == -1:
        break
    ans = w_dp(a, b, c)
    print(f'w(%d, %d, %d) = %d'%(a, b, c, ans))