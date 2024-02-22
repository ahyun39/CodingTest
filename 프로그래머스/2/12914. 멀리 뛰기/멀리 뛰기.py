def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    return dp[n]