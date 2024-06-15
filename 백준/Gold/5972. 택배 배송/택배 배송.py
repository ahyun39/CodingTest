import heapq

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

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

print(dijkstra(1,n,graph)[n])