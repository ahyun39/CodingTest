k = int(input())
nums = []
for _ in range(k):
    jam = int(input())
    if jam == 0:
        nums.pop()
    else:
        nums.append(jam)
print(sum(nums))