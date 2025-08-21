# 4485_녹색 옷 입은 애가 젤다지?_골드4
import heapq

d = [(-1,0), (1,0), (0,-1), (0,1)]
INF = int(1e9)

def dijkstra(n, graph):
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = graph[0][0]
    pq = [(graph[0][0], 0, 0)]

    while pq:
        cost, x, y = heapq.heappop(pq)
        if dist[x][y] < cost:
            continue
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = graph[nx][ny] + cost
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    return dist[n-1][n-1]

def main():
    t = 1
    while True:
        n = int(input())
        if n == 0: break
        graph = [list(map(int, input().split())) for _ in range(n)]
        ans = dijkstra(n, graph)
        print(f"Problem {t}: {ans}")
        t += 1

if __name__ == "__main__":
    main()