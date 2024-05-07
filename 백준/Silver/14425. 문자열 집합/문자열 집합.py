n, m = map(int,input().split())
ans = 0
words = {}
for _ in range(n):
    words[input()] = 0
for _ in range(m):
    word = input()
    if word in words: words[word] += 1
print(sum(v for v in words.values() if v >= 1))