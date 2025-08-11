from collections import deque

N, M = map(int, input().split())
graph = [str(input()) for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]

sx, sy = -1, -1

for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            sx, sy = i, j
            break
    if sy != -1: break

meet_people = 0
d = [(-1, 0,), (1, 0), (0, -1), (0, 1)]

q = deque()
q.append((sx, sy))
visited[sx][sy] = True

while q:
    x, y = q.popleft()
    
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny]!= 'X':
            visited[nx][ny] = True
            q.append((nx, ny))
            if graph[nx][ny] == 'P':
                meet_people += 1

print(meet_people if meet_people > 0 else "TT")