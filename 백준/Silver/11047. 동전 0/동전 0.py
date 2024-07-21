n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
cnt = 0

for i in range(n):
    if coins[i] <= k:
        cnt += k // coins[i]
        k %= coins[i]
    if k == 0:
        break
print(cnt)