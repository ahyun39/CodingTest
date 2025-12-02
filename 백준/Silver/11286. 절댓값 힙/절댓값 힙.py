import heapq

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)