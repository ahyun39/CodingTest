import heapq

n = int(input())
numbers = []
max_heap = []
for _ in range(n):
    ord = int(input())
    if ord == 0:
        if max_heap == []:
            numbers.append(0)
        else:
            numbers.append(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap,(-ord,ord))
for num in numbers:
    print(num)