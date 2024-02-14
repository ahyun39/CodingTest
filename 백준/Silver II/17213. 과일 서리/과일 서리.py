N = int(input())
M = int(input()) - N

def calculate_combination(n, r):
    result = 1
    for i in range(r):
        result *= n
        n -= 1
        result //= (i + 1)
    return result

if N - 1 < M:
    ans = calculate_combination(N - 1 + M, N - 1)
else:
    ans = calculate_combination(N - 1 + M, M)

print(ans)