from collections import deque

def find_ice_locations(graph, N, M):
    return 

def melt_iceberg(graph, N, M, ice_locations):
    melted_graph = [[0] * M for _ in range(N)]
    new_locations = []
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    
    for x, y in ice_locations:
        sea_cnt = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                sea_cnt += 1
        melted_graph[x][y] = max(0, graph[x][y] - sea_cnt)
        if melted_graph[x][y] > 0:
            new_locations.append((x, y))
    
    return new_locations, melted_graph

def count_iceberg_groups(graph, N, M, ice_locations):
    visited = [[False] * M for _ in range(N)]
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    groups = 0

    def bfs(start_x, start_y):
        q = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < N and 0 <= ny < M and 
                    graph[nx][ny] > 0 and not visited[nx][ny]):
                    q.append((nx, ny))
                    visited[nx][ny] = True

    for x, y in ice_locations:
        if graph[x][y] > 0 and not visited[x][y]:
            bfs(x, y)
            groups += 1
    
    return groups

def main():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ice_locations = [(i, j) for i in range(N) for j in range(M) if graph[i][j] > 0]
    for days in range(1, 1001):
        ice_locations, graph = melt_iceberg(graph, N, M, ice_locations)
        iceberg_groups = count_iceberg_groups(graph, N, M, ice_locations)
        
        if iceberg_groups >= 2:
            return days
    
    return 0

if __name__ == "__main__":
    print(main())