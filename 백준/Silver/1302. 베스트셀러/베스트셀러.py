n = int(input())
sells = {}
for _ in range(n):
    book = str(input())
    sells[book] = sells.get(book,0) + 1
ans = [k for k,v in sells.items() if max(sells.values()) == v]
ans.sort()
print(ans[0])