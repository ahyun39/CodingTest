import sys
from collections import defaultdict
input = sys.stdin.readline

S = input().strip()
q = int(input())

n = len(S)
chars = set(S)
char_cnt = defaultdict(lambda:[0]*(n+1))

for i, c in enumerate(S):
    for ch in chars:
        char_cnt[ch][i+1] = char_cnt[ch][i]
    char_cnt[c][i+1] += 1

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(char_cnt[a][r+1] - char_cnt[a][l])