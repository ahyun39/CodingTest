import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False 
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2): 
        if n % i == 0:
            return False
    return True

t = int(input())
decimals = []
for _ in range(t):
    num = int(input())
    while True:
        if is_prime(num):
            decimals.append(num)
            break
        num += 1
print(*decimals, sep='\n')