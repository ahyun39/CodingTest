n, k = map(int,input().split())
i = 1
while i < n:
    k //= 2
    i += 1
print(k)