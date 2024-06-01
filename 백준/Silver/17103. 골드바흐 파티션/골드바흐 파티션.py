def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]

def count_prime_pairs(num):
    primes = sieve_of_eratosthenes(num)
    cnt = 0
    left, right = 0, len(primes) - 1
    while left <= right:
        total = primes[left] + primes[right]
        if total == num:
            cnt += 1
            left += 1
            right -= 1
        elif total < num:
            left += 1
        else:
            right -= 1
    return cnt

t = int(input())
for _ in range(t):
    num = int(input())
    print(count_prime_pairs(num))