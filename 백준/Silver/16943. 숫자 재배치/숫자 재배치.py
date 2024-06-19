from itertools import permutations

a, b = map(str,input().split())
permu = list(permutations(list(a), len(a)))
permu.sort(reverse=True)
ans = -1
for p in permu:
    if p[0] != "0":
        if int(''.join(p)) < int(b):
            ans = int(''.join(p))
            break
print(ans)