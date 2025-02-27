def bellman(V, edges, start):
    INF = float('inf')
    dist = [INF] * (V+1)
    dist[start] = 0

    for _ in range(V+1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return -1
        
    for i in range(V+1):
        if dist[i] == INF:
            dist[i] = -1

    return dist
        
def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    start = 1
    dist = bellman(N, edges, start)
    if dist == -1:
        print(dist)
    else:
        print(*dist[2:], sep='\n')

if __name__ == "__main__":
    main()