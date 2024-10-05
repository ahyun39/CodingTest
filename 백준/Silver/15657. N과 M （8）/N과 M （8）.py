n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def back():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(n):
        if ans:
            if ans[-1] <= nums[i]:
                ans.append(nums[i])
                back()
                ans.pop()
        else:
            ans.append(nums[i])
            back()
            ans.pop()
    return
back()