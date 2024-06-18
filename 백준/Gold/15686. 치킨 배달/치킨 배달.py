from itertools import combinations

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

homes = [(i,j) for i in range(n) for j in range(n) if graph[i][j] == 1]
chickens = [(i,j) for i in range(n) for j in range(n) if graph[i][j] == 2]
min_dist = float('inf')
for comb in combinations(chickens, m):
    dist_ = 0
    for h in homes:
        dist = float('inf')
        for c in comb:
            if dist > (abs(h[0] - c[0]) + abs(h[1] - c[1])):
                dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
        dist_ += dist
    if min_dist > dist_:
        min_dist = dist_
print(min_dist)