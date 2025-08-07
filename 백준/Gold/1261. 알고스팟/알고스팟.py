from collections import deque

M, N = map(int, input().split())  # M: 열, N: 행
graph = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우 이동
d = [(-1,0),(1,0),(0,-1),(0,1)]

# 벽 부순 최소 횟수를 저장하는 dist 배열
dist = [[-1]*M for _ in range(N)]
dist[0][0] = 0

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            # 아직 방문 안 했거나 더 나은 경로 발견 시
            if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + graph[nx][ny]:
                dist[nx][ny] = dist[x][y] + graph[nx][ny]
                # 벽이 아닌 경우 먼저 탐색
                if graph[nx][ny] == 0:
                    q.appendleft((nx, ny))
                else:
                    q.append((nx, ny))

print(dist[N-1][M-1])