n = int(input())
stair = [int(input()) for _ in range(n)] + [0]*(301-n)

dp = [0] * 301
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2]+stair[i])

print(dp[n-1])