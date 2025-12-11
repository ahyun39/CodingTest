#7569_토마토

from collections import deque

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]
ans = 0

for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

for g in graph:
    for row in g:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit()
        ans = max(ans, max(row))

print(ans - 1)