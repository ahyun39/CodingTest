def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
ra, rb = (a1 * b2) + (a2 * b1), (b1 * b2)

g = gcd(ra, rb)
ra //= g
rb //= g

print(ra, rb)