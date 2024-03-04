n = int(input())
words = [sorted(list(str(input()))) for _ in range(n)]
ans = 0
for i in range(1,n):
    t = words[i].copy()
    k = words[0].copy()
    for j in range(len(words[i])):
        if words[i][j] in k: 
            k.remove(words[i][j])
            t.remove(words[i][j])
    if len(k) <= 1 and len(t) <= 1: ans += 1
print(ans)