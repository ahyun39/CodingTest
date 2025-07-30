# 1753_최단경로_골드4

import heapq

INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for i in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(v+1):
    if distance[i] == INF:
        distance[i] = 'INF'

print(*distance[1:], sep='\n')