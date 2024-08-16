from collections import deque

def bfs(x, y, n, m, graph, visited):
    q = deque([])
    q.append((x, y))
    area = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area

def solution():
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]

    picture_cnt, max_area = 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                picture_cnt += 1
                area = bfs(i, j, n, m, graph, visited)
                if max_area < area:
                    max_area = area
    print(picture_cnt)
    print(max_area)

solution()