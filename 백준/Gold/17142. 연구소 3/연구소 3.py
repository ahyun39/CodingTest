from itertools import combinations
from collections import deque
import copy

n, m = map(int,input().split())
ori_board = [list(map(int,input().split())) for _ in range(n)]

virus = [(i,j) for i in range(n) for j in range(n) if ori_board[i][j] == 2]

for i in range(n):
    for j in range(n):
        if ori_board[i][j] == 1:
            ori_board[i][j] = "-"

def bfs(q, ori_board, visited):
    board = [row[:] for row in ori_board]
    pq = copy.deepcopy(q)
    for x, y in virus:
        board[x][y] = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny]:
                if (nx,ny) not in pq:
                    board[nx][ny] = board[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
                
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != "-" and (i,j) not in virus:
                cnt = max(cnt, board[i][j])
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and (i,j) not in pq and (i,j) not in virus:
                return float("inf")
    return cnt

ans = float("inf")
for p in combinations(virus,m):
    # p 는 바이러스 조합
    p = deque(p)
    visited = [[False]*n for _ in range(n)]
    cnt = bfs(p, ori_board, visited)
    if cnt < ans:
        ans = cnt
print(ans if ans != float("inf") else -1)