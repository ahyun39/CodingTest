n = int(input())
def fac(n):
    if n-1 > 0:
        return n * fac(n-1)
    else:
        return n
if n == 0: print(1)
else: print(fac(n))