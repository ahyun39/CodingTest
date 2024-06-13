from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
cnt = list(Counter(nums).items())
max_cnt = max(list(Counter(nums).values()))

ma = [x for x in cnt if x[1] == max_cnt]
if len(ma) == 1:
    cnt_ma = ma[0][0]
elif len(ma):
    cnt_ma = ma[1][0]
print(round(sum(nums)/n))
print(nums[n//2])
print(cnt_ma)
print(nums[-1] - nums[0])