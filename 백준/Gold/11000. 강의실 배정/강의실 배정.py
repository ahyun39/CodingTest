import heapq

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x: x[0])
heap = []
heapq.heappush(heap, classes[0][1])

for i in range(1, n):
    # 현재 강의의 시작 시간보다 일찍 끝나는 강의를 제거
    if classes[i][0] >= heap[0]:
        heapq.heappop(heap)
    # 현재 강의의 종료 시간을 힙에 추가
    heapq.heappush(heap, classes[i][1])
print(len(heap))