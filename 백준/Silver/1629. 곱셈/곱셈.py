import sys
sys.setrecursionlimit(10**5)

A, B, C = map(int ,input().split())

def recur(b):
    if b == 0:
        return 1
    half = recur(b // 2)
    half = (half * half) % C
    if b % 2 == 1:
        half = (half * A) % C
    return half

answer = recur(B)
print(answer)
