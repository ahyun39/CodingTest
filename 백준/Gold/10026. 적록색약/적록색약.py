from collections import deque

def check_zone(n, graph):
    zone = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                zone += 1
                bfs(i, j, graph[i][j], visited, n, graph)
    return zone

def bfs(x, y, color, visited, n, graph):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and color == graph[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

def color_switch(graph, n):
    for i in range(n):
        graph[i] = graph[i].replace("R", "G")
    return graph

def main():
    n = int(input())
    graph = [input() for _ in range(n)]
    color_not_blindness, color_blindness = check_zone(n, graph), check_zone(n, color_switch(graph, n))
    return color_not_blindness, color_blindness
print(*main())