def f():
    N, P, Q = map(int, input().split())
    dp = {0:1}

    def dfs(n):
        if n in dp:
            return dp[n]
        dp[n] = dfs(n // P) + dfs(n // Q)
        return dp[n]

    print(dfs(N))

f()