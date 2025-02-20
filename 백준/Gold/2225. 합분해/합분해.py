def f():
    N, K = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # k=1일 때 초기값 설정
    for n in range(N + 1):
        dp[1][n] = 1

    # DP 계산 (누적 합 활용)
    for k in range(2, K + 1):
        dp[k][0] = 1  # n=0인 경우, 한 가지 방법만 존재
        for n in range(1, N + 1):
            dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % 1000000000

    print(dp[K][N])

f()