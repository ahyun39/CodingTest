import heapq
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    M = int(input().strip())

    # 안전하게 M개의 정수를 읽기 (여러 줄에 걸쳐 올 수 있음)
    nums = []
    while len(nums) < M:
        nums.extend(map(int, input().split()))

    left = []   # max-heap
    right = []  # min-heap

    medians = []
    for i, x in enumerate(nums, start=1):
        if not left or x <= -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)

        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))
        if i % 2 == 1:
            medians.append(-left[0])

    print(len(medians))
    for i in range(0, len(medians), 10):
        print(*medians[i:i+10])