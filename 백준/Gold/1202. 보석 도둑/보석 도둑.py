#1202_보석 도둑
import heapq

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x:x[0])
bags.sort()

max_heap = []
ans = 0
idx = 0

for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(max_heap, -jewels[idx][1])
        idx += 1
    if max_heap:
        ans += -heapq.heappop(max_heap)

print(ans)