import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))

def dijkstra(start, n, graph):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return distance

start, end = map(int,input().split())
print(dijkstra(start, n, graph)[end])