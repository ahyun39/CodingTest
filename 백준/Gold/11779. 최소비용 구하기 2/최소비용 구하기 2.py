# 11779_최소비용 구하기 2_골드3

import heapq
from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


start, end = map(int, input().split())

def dijkstra(start, end):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    parent = {start: None}

    pq = [(0, start)]

    while pq:
        cur_dist, node = heapq.heappop(pq)

        if cur_dist > dist[node]:
            continue
        
        if node == end:
            break
        
        for nxt, weight in graph[node]:
            new_dist = cur_dist + weight
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                parent[nxt] = node
                heapq.heappush(pq, (new_dist, nxt))
                
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()

    return dist[end], len(path), path

ans = dijkstra(start, end)

print(ans[0])
print(ans[1])
print(*ans[2])