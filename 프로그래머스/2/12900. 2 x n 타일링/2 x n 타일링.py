MOD = 1000000007

def precompute_factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    return fact, inv_fact

def solution(n):
    fact, inv_fact = precompute_factorials(n, MOD)
    answer = 0
    
    for i in range(n // 2 + 1):
        a_block = i
        b_block = n - 2 * i
        if b_block >= 0:
            total = fact[a_block + b_block] * inv_fact[a_block] % MOD * inv_fact[b_block] % MOD
            answer = (answer + total) % MOD
    
    return answer
