import heapq

def solve():
    n, m = map(int,input().split())
    
    visibility = list(map(int, input().split()))
    
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int,input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(start):
        distances = [float('inf')] * n
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            dist, now = heapq.heappop(pq)
            
            if dist > distances[now]:
                continue
            
            for neighbor, weight in graph[now]:
                if visibility[neighbor] == 1 and neighbor != n-1:
                    continue
                distance = dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances[n-1]
    
    result = dijkstra(0)
    print(result if result != float('inf') else -1)

solve()