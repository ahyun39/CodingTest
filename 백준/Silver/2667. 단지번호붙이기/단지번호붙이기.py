from collections import deque

def bfs(graph, i, j, visited):
    q = deque([(i, j)])
    cnt = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == '1':
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
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
                apartment.append(bfs(graph, i, j, visited))
    apartment.sort()
    print(len(apartment))
    print(*apartment, sep='\n')

f()