def dfs(graph, x, y, visited):
    visited[x][y] = True
    cnt = 1  # 현재 위치 포함
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == '1':
            cnt += dfs(graph, nx, ny, visited)  # 연결된 노드 탐색
    return cnt

def f():
    global N
    N = int(input())
    graph = [input() for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    apartment = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '1' and not visited[i][j]:
                apartment.append(dfs(graph, i, j, visited))

    apartment.sort()
    print(len(apartment))
    print(*apartment, sep='\n')

f()