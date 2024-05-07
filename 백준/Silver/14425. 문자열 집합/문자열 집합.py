n, m = map(int,input().split())
ans = 0
words = {}
for _ in range(n):
    word = str(input())
    words[word] = 0
for _ in range(m):
    word = str(input())
    if word in words:
        words[word] += 1
for v in words.values():
    if v >= 1: ans += v
print(ans)