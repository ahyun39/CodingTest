t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    if n in [1, 2, 3]:
        print(1)
    else:
        dp[1], dp[2], dp[3] = 1, 1, 1
        for i in range(4,n+1):
            dp[i] = dp[i-3] + dp[i-2]
        print(dp[n])