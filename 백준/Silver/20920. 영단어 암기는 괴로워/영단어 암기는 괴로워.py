from collections import Counter

n, m = map(int,input().split())
words = []
for _ in range(n):
    word = str(input())
    if len(word) >= m: words.append(word)
wordbook = list(Counter(words).items())
wordbook.sort(key=lambda x:(-x[1],-len(x[0]),x[0]))
for w in wordbook:
    print(w[0])