from collections import deque

def mark_box(m, n, boxes):
    graph = [[1]*n for _ in range(m)]
    for lx, ly, rx, ry in boxes:
        for i in range(m-ry, m-ly):
            for j in range(lx, rx):
                graph[i][j] = 0
    return graph

def bfs(x, y, m, n, visited, graph):
    q = deque([])
    q.append((x, y))
    area = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area

def solution():
    m, n, k = map(int,input().split())
    boxes = [list(map(int,input().split())) for _ in range(k)]
    graph = mark_box(m, n, boxes)
    visited = [[False] * n for _ in range(m)]

    cnt = 0
    area_list = []

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                area = bfs(i, j, m, n, visited, graph)
                cnt += 1
                area_list.append(area)
    area_list.sort()
    
    print(cnt)
    print(*area_list)

if __name__ == "__main__":
    solution()