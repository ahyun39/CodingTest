def atm():
    N = int(input())
    times = list(map(int, input().split()))
    times.sort()

    ans = 0
    for i in range(N):
        ans += sum(times[:i+1])
    return ans

print(atm())