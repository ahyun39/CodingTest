def binary_search(liquids, N):
    left, right = 0, N - 1
    min_diff, ans = float('inf'), [0, 0]

    while left < right:
        liquid_sum = liquids[left] + liquids[right]
        if min_diff > abs(liquid_sum):
            min_diff = abs(liquid_sum)
            ans = [liquids[left], liquids[right]]
        if liquid_sum < 0:
            left += 1
        else:
            right -= 1

    return ans

def f():
    N = int(input())
    liquids = sorted(list(map(int, input().split())))
    print(*binary_search(liquids, N))

f()