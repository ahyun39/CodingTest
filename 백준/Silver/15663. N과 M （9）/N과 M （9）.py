from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = set()
for permu in permutations(nums, m):
    result.add(tuple(permu))
result = list(result)
result.sort()
for res in result:
    print(*res)