from collections import Counter

S = str(input())
q = int(input())
for _ in range(q):
    a, l, r = map(str, input().split())
    l, r = int(l), int(r)
    sub = S[l:r+1]
    counter = Counter(sub)
    if a in counter:
        print(counter[a])
    else:
        print(0)