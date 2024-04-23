import heapq

n = int(input())
heap = []
ans = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            ans.append(heapq.heappop(heap))
        else:
            ans.append(0)
    else:
        heapq.heappush(heap,x)
for a in ans:
    print(a)