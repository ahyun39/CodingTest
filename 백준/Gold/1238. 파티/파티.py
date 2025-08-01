import heapq

INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(M):
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

max_dist = -1

distance = [INF] * (N+1)
dijkstra(X)
distance_x = distance

for i in range(1, N+1):
    distance = [INF] * (N+1)
    dijkstra(i)
    if max_dist < distance[X] + distance_x[i]:
        max_dist = distance[X] + distance_x[i]

print(max_dist)