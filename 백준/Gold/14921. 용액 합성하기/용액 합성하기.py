def solution():
    n = int(input())
    liquids = list(map(int, input().split()))

    lo, hi = 0, n - 1
    min_mix = float('inf')
    ans = [0, 0]

    while lo < hi:
        mix = liquids[lo] + liquids[hi]
        if abs(mix) < min_mix:
            min_mix = abs(mix)
            ans = [liquids[lo], liquids[hi]]
        
        if mix < 0:
            lo += 1
        else:
            hi -= 1

    print(sum(ans))

if __name__ == "__main__":
    solution()