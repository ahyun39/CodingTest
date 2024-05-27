n = int(input())
nums = list(map(int,input().split()))
temp = set(nums)
ttemp = list(temp)
ttemp.sort()
compression = {}
for i, v in enumerate(ttemp):
    compression[v] = i
nums = [compression[nums[i]] for i in range(n)]
print(*nums)