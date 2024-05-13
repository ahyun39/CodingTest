n = int(input())
distances = list(map(int,input().split())) + [0]
oils = list(map(int,input().split()))

# dp[i]: i번째 주유소까지 도달하는데 필요한 최소 비용
dp = [float('inf')] * (n+1)
dp[0] = 0

for i in range(n):
    cost = 0
    for j in range(i, n):
        cost += distances[j] * oils[i]
        dp[j + 1] = min(dp[j + 1], dp[i] + cost)
print(dp[n])