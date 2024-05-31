from collections import deque

r, c = map(int, input().split())
farm = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
wolves = deque()

for i in range(r):
    for j in range(c):
        if farm[i][j] == "W":
            wolves.append((i, j))
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ax, ay = i + dx, j + dy
                if 0 <= ax < r and 0 <= ay < c and farm[ax][ay] == ".":
                    farm[ax][ay] = "D"

def bfs():
    while wolves:
        x, y = wolves.popleft()
        for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if farm[nx][ny] == "S":
                    return False
                if farm[nx][ny] == ".":
                    visited[nx][ny] = True
                    wolves.append((nx, ny))
    return True

for i in range(r):
    for j in range(c):
        if farm[i][j] == "W":
            visited[i][j] = True

ans = bfs()

print(1 if ans else 0)
for f in farm:
    print(''.join(f))
