def solution(triangle):
    answer = 0
    dp = [[0]*i for i in range(1,len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if 0 <= j - 1 < len(triangle[i-1]) and j < len(triangle[i-1]) :
                dp[i][j] = max(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])
            else:
                if j >= len(triangle[i-1]):
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
    
    return max(dp[-1])