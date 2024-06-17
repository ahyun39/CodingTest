from collections import deque
from itertools import combinations

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = float('inf')
prices = []
for i in range(1,n-1):
    for j in range(1,n-1):
        x, y = i, j
        cnt = graph[x][y] + graph[x][y-1] + graph[x-1][y] + graph[x][y+1] + graph[x+1][y]
        prices.append((x, y, cnt))

for c in combinations(prices, 3):
    visited = [[False] * n for _ in range(n)]
    k = 0
    for x, y, cnt in c:
        if not visited[x][y] and not visited[x-1][y] and not visited[x][y-1] and not visited[x][y+1] and not visited[x+1][y]:
            visited[x][y] = True
            visited[x-1][y] = True
            visited[x][y-1] = True
            visited[x][y+1] = True
            visited[x+1][y] = True
            k += cnt
        else:
            k = float('inf')
            break
    if k < ans:
        ans = k
print(ans)