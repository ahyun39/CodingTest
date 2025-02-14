import heapq

def meeting_room():
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    meetings.sort()
    pq = []
    heapq.heappush(pq, meetings[0][1])
    
    for i in range(1, N):
        start, end = meetings[i]
        if pq[0] <= start:
            heapq.heappop(pq)
        heapq.heappush(pq, end)
    return len(pq)

print(meeting_room())