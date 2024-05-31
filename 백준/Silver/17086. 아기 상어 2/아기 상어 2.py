from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j]:
            q.append((i, j))
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < n and 0<= ny < m and board[nx][ny]==0:
                board[nx][ny] = board[x][y]+1
                q.append((nx, ny))
bfs()
print(max(map(max, board))-1)