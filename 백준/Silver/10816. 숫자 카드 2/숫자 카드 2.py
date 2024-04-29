from collections import Counter
n = int(input())
ncards = list(map(int,input().split()))
m = int(input())
mcards = list(map(int,input().split()))

cnt = Counter(ncards)
ans = []
for card in mcards:
    ans.append(cnt.get(card,0))
print(*ans)