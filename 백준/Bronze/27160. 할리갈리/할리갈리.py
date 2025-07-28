N = int(input())
cards = {}

for _ in range(N):
    fruit, cnt = map(str, input().split())
    if fruit in cards: cards[fruit] += int(cnt)
    else: cards[fruit] = int(cnt)

if 5 in cards.values():
    print("YES")
else:
    print("NO")