from collections import Counter

N, M = map(int,input().split())
DNA = [str(input()) for _ in range(N)]

s = ['d' for _ in range(M)]
hamming_dist = 0

for i in range(M):
    alpha = []
    for j in DNA:
        alpha.append(j[i])
    a = Counter(alpha)
    a = sorted(a.items(),key=lambda x:(-x[1],x[0]))
    s[i] = a[0][0]
    hamming_dist += (N - a[0][1])
print(''.join(s))
print(hamming_dist)