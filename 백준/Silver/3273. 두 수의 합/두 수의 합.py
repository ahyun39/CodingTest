n = int(input())
nums = list(map(int, input().split()))
find_num = int(input())

nums.sort()

cnt = 0

l, r = 0, n-1
while l < r:
    if nums[l] + nums[r] == find_num:
        cnt += 1
        l += 1
    elif nums[l] + nums[r] > find_num:
        r -= 1
    else:
        l += 1
print(cnt)