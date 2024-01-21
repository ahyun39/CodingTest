T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    a, b = max(n,m), min(n,m)
    x, y = 1, 1
    for i in range(b):
        x *= a
        a -= 1
        y *= b
        b -= 1
    print(x // y)