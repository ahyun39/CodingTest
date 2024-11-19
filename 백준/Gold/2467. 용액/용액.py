def solution():
    n = int(input())
    liquids = list(map(int, input().split()))

    lo, hi = 0, n-1
    mix = float('inf')
    ans = [0, 0]
    while lo < hi:
        liquids_mix = liquids[lo] + liquids[hi]
        if abs(liquids_mix) < mix:
            mix = abs(liquids_mix)
            ans = [liquids[lo], liquids[hi]]
        if liquids_mix < 0:
            lo += 1
        else:
            hi -= 1
    print(*ans)

if __name__ == "__main__":
    solution()