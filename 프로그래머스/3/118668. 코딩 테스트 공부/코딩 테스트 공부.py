def solution(alp, cop, problems):
    # 목표(최댓값) 계산: 이 이상이면 모든 문제를 풀 수 있음9
    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)
    
    # 초기값이 이미 목표보다 크면 범위를 넘치지 않게 클램핑
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    INF = 10**9
    # dp[a][c] = 최소 시간
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    
    # DP 전개: (a, c)에서 가능한 모든 행동으로 상태 갱신
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            # 현재 상태까지의 최소 시간
            cur = dp[a][c]
            if cur == INF:
                continue
                
            # 공부: 알고력 + 1
            if a + 1 <= max_alp:
                if dp[a+1][c] > cur + 1:
                    dp[a+1][c] = cur + 1
            # 코딩 연습: 코딩력 + 1
            if c + 1 <= max_cop:
                if dp[a][c+1] > cur + 1:
                    dp[a][c+1] = cur + 1
            # 각 문제 풀기 (요구치 만족하면)
            for reqA, reqC, rewA, rewC, cost in problems:
                if a >= reqA and c >= reqC:
                    na = min(max_alp, a + rewA)
                    nc = min(max_cop, c + rewC)
                    if dp[na][nc] > cur + cost:
                        dp[na][nc] = cur + cost
    return dp[max_alp][max_cop]