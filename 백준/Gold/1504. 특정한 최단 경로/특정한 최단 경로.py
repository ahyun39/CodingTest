import heapq

INF = int(1e9)

def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
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

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 1번 노드부터 시작하는 최단 경로
dist_from_start = dijkstra(1, n, graph)

# v1 노드부터 시작하는 최단 경로
dist_from_v1 = dijkstra(v1, n, graph)

# v2 노드부터 시작하는 최단 경로
dist_from_v2 = dijkstra(v2, n, graph)

path1 = dist_from_start[v1] + dist_from_v1[v2] + dist_from_v2[n]
path2 = dist_from_start[v2] + dist_from_v2[v1] + dist_from_v1[n]

answer = min(path1, path2)

if answer >= INF:
    print(-1)
else:
    print(answer)