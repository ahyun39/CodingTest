import math

M, N = map(int,input().split())

def primenum(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

for num in range(M, N+1):
    if primenum(num) and num != 1: print(num)