# 1759_암호 만들기_골드5

from itertools import combinations

L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()

vowel_list = ["a", "e", "i", "o", "u"]

for combi in combinations(alphabet, L):
    vowel_cnt = 0
    for alpha in combi:
        if alpha in vowel_list: vowel_cnt += 1
    consonant_cnt = L - vowel_cnt
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        print(''.join(combi))