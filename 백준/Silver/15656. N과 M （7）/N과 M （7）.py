n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def back():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(n):
        ans.append(nums[i])
        back()
        ans.pop()
    return
back()