from collections import deque

def bfs(x, y, n, visited, graph):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return

def raining(mm, n, graph):
    region_status = [[1 if graph[i][j] <= mm else 0 for j in range(n)] for i in range(n)]
    cnt = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if region_status[i][j] == 0 and not visited[i][j]:
                cnt += 1
                bfs(i, j, n, visited, region_status)
    return cnt

def solution():
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]

    max_rains = max(map(max, graph))
    max_area = 0

    for i in range(0, max_rains + 1):
        cnt = raining(i, n, graph)
        if max_area < cnt:
            max_area = cnt
    return max_area

if __name__ == "__main__":
    print(solution())