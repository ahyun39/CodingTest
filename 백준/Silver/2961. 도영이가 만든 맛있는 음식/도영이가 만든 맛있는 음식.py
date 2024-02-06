from itertools import combinations 
N = int(input())
ingredient = [list(map(int,input().split())) for _ in range(N)]
mix = [list(combinations(ingredient,i)) for i in range(1,N+1)]
ans = 1e9
for m in mix:
    for i in range(len(m)):
        a, b = 1, 0
        for j in range(len(m[i])):
            a *= m[i][j][0]
            b += m[i][j][1]
        if abs(a-b) < ans: ans = abs(a-b)
print(ans)