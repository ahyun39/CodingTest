n = int(input())
dp = [0] * (1000001)
dp[1], dp[2], dp[3] = 1, 2, 3
if n > 3:
    for i in range(4,n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
    print(dp[n] % 15746)
else:
    print(dp[n])