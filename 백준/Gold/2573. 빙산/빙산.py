from collections import deque

# 빙산 녹는것
def melt_iceberg(graph, N, M):
    new_graph = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                sea_cnt = 0
                for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        sea_cnt += 1
                new_graph[i][j] = max(0, graph[i][j] - sea_cnt)
    return new_graph

# 빙산 덩어리 구하기
def count_iceberg(graph, N, M):
    iceberg = 0
    global visited
    visited = [[False] * (M) for _ in range(N)]

    def bfs(graph, i, j):
        q = deque([(i, j)])
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(graph, i, j)
                iceberg += 1
    
    return iceberg

def main():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    days = 0
    max_day = 1000
    while max_day > 0:
        graph = melt_iceberg(graph, N, M)
        iceberg = count_iceberg(graph, N, M)
        days += 1
        max_day -= 1
        if iceberg >= 2:
            return days
    return 0

if __name__ == "__main__":
    print(main())