n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
diff = {}
for i in a:
    diff[i] = diff.get(i,0) + 1
for i in b:
    diff[i] = diff.get(i,0) + 1
for v in diff.values():
    if v == 1: ans += 1
print(ans)