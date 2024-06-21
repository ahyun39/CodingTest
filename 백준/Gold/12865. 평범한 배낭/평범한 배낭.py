n, k = map(int, input().split())
objects = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k + 1)

for weight, value in objects:
    for current_weight in range(k, weight - 1, -1):
        dp[current_weight] = max(dp[current_weight], dp[current_weight - weight] + value)

print(dp[k])