def atm():
    N = int(input())
    times = list(map(int, input().split()))
    times.sort()

    ans = sum([sum(times[:i+1]) for i in range(N)])
    return ans

print(atm())