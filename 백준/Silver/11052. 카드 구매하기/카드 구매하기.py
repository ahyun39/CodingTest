n = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
cards_idx = [[i,v] for i, v in enumerate(cards)]
for i in range(1,n+1):
    for j in range(i):
        dp[i] = max(dp[i-j]+dp[j],cards[i],dp[i])
print(dp[n])