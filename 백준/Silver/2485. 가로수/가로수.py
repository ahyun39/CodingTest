import math
n = int(input())
trees = [int(input()) for _ in range(n)]
gaps = []
for i in range(n-1):
    gaps.append(trees[i+1] - trees[i])

def gcd_n(gaps):
    g = gaps[0]
    for item in gaps:
        g = math.gcd(g, item)
    return g
gcd = gcd_n(gaps)

ans = 0
for g in gaps:
    ans += (g // gcd) - 1
print(ans)