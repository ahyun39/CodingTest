#1860_부분합

N, S = map(int ,input().split())
nums = list(map(int, input().split()))

left = 0
cur_sum = 0
ans = N+2

for right in range(N):
    cur_sum += nums[right]
    while cur_sum >= S:
        ans = min(ans, right - left + 1)
        cur_sum -= nums[left]
        left += 1

print(0 if ans == N+2 else ans)