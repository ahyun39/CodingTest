import sys

def cantor_set(n):
    if n == 0:
        return '-'
    prev = cantor_set(n - 1)
    return prev + ' ' * len(prev) + prev

while True:
    try:
        N = int(input().strip())
        result = cantor_set(N)
        print(result)
    except EOFError: break