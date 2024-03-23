def solution(money):
    answer = 0
    dp = [0] * len(money)
    dp[0], dp[1] = money[0], max(money[0],money[1])
    for i in range(2,len(money)-1):
        dp[i] = max(dp[i-1],dp[i-2]+money[i])
    
    new_dp = [0] * (len(money))
    new_dp[0], new_dp[1] = 0, money[1]
    for i in range(2,len(money)):
        new_dp[i] = max(new_dp[i-1],new_dp[i-2]+money[i])

    return max(max(dp),max(new_dp))