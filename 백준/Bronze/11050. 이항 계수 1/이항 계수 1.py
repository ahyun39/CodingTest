n, k = map(int,input().split())
a, b = 1, 1
for _ in range(k):
    a *= n
    n -= 1
while k > 0:
    b *= k
    k -= 1
print(int(a/b))