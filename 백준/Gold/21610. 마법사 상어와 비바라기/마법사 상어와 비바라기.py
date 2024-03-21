n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
order = [list(map(int,input().split())) for _ in range(m)]

directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

cloud = [[0]*n for _ in range(n)] # 이동전 구름
move_cloud = [[0]*n for _ in range(n)] # 이동한 구름
for i, j in [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]:
    cloud[i][j] = 1

def is_valid(x,y):
    return 0 <= x < n and 0 <= y < n

def move(x,y,d,s):
    dx, dy = directions[d-1][0], directions[d-1][1]
    nx, ny = (x + s*dx)%n, (y + s*dy)%n
    cloud[x][y], move_cloud[nx][ny]  = 0, 1
    board[nx][ny] += 1
    return

def water_copy(x,y):
    for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx,ny) and board[nx][ny] > 0:
            board[x][y] += 1
    return

for d, s in order:
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                move(i,j,d,s)
    for i in range(n):
        for j in range(n):
            if move_cloud[i][j] == 1:
                water_copy(i,j)
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and move_cloud[i][j] != 1:
                cloud[i][j] = 1
                board[i][j] -= 2
            if move_cloud[i][j] == 1:
                move_cloud[i][j] = 0
answer = sum([sum(b) for b in board])
print(answer)