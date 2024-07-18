n, k = map(int, input().split())
nums = list(map(int, input().split()))

current_sum = sum(nums[:k])
max_sum = current_sum

for i in range(1, n - k + 1):
    current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)