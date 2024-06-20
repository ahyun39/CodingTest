n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            continue
        
        if y > 0:
            dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]
        
        if x > 0:
            dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]
        
        if x > 0 and y > 0 and graph[x-1][y] == 0 and graph[x][y-1] == 0:
            dp[x][y][2] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]

ans = dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2]
print(ans)